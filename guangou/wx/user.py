from django.shortcuts import render, HttpResponse
from wx import models
from django.views.decorators.csrf import csrf_exempt
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from wx.util.typeMap import *
from wx.util.db import *
# Create your views here.


def addUser(request: HttpRequest):
    # usertypeid_for = models.UserType.objects.get(usertypeid=1)
    # user_obj = models.User(
    #     username = '赵云',
    #     identitynumber = '23023019830522176X',
    #     usertypeid = usertypeid_for,
    #     phonenumber = '17811115555',
    #     nickname = '嘿嘿嘿',
    #     password = 'C33367701511B4F6020EC61DED352059',
    #     openid = 'wx15641464845315256',
    #     isvaild = '1',
    # )
    # user_obj.save()

    # models.User.objects.update_or_create(
    #     userid=12,
    #     defaults={
    #         'username' : '诸葛亮',
    #         'nickname' : '嘿嘿嘿',
    #         'isvaild':1,
    #     }
    # )

    usertypeid_for = models.UserType.objects.get(usertypeid=1)
    models.User.objects.update_or_create(
        userid=15,
        defaults={
            'username': '孙权',
            'nickname': '哗哗哗',
            'usertypeid': usertypeid_for,
            'phonenumber': '13856884612',
            'studentid': '2017564656',
            'isvaild': 0,
        }
    )

    return HttpResponse('ok')


def getUser(request: HttpRequest):
    # user_list=models.User.objects.all()
    # print(user_list[0].username) #索引取值
    # print(user_list[0:3]) #切片取值

    # user_list=models.User.objects.filter(userid=4)
    # print(user_list[0].username)

    user = models.User.objects.get(userid=4)
    print(user.username)

    return HttpResponse('ok')


def updateUser(request: HttpRequest):
    # obj=models.User.objects.get(userid=11)
    # print(obj.username)
    # obj.title='刘备'
    # obj.nickname='hhh'
    # obj.isvaild=1
    # obj.save()

    # models.User.objects.update(
    #     studentid='201811112222',
    #     nickname='Wahhhhhh'
    # )
    # models.User.objects.all().update(
    #     studentid='201800001111',
    #     nickname='lalalala'
    # )

    obj = models.User.objects.filter(username='赵云').update(
        studentid='20182222',
        nickname='zaoyun'
    )
    print(obj)

    return HttpResponse('ok!')


def deleteUser(request: HttpRequest):
    obj = models.User.objects.get(userid=11).delete()
    print(obj)

    return HttpResponse('ok')


"""
 @api {get} /wx/user/getUserInfo 获取用户信息（昵称、打卡次数）
 @apiName /user/getUserInfo
 @apiGroup User

 @apiParam {String} openid 用户openid (如：'wx9a3377455576ee6c')

 @apiSampleRequest /wx/user/getUserInfo
"""
@csrf_exempt
def getUserInfo(request: HttpRequest):
    res = {}
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)
    openid = request.GET.get("openid")
    if openid is None:
        # 新增用户（待写）
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)

    obj = models.User.objects.get(openid=openid)
    res['data'] = {'checkintimes': obj.checkintimes,
                   'nickname': obj.nickname}
    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


"""
 @api {get} /wx/user/getUserCollectedVenue 获取用户收藏的总场馆
 @apiName /user/getUserCollectedVenue
 @apiGroup User

 @apiParam {String} openid 用户openid (如：'wx9a3377455576ee6c','wx9a3377455576ee6b')
 @apiParam {decimal} longitude 用户所在位置的经度(如：116.346352)
 @apiParam {decimal} latitude  用户所在位置的纬度(如：39.960501)
 @apiParam {int} page  页码

 @apiSampleRequest /wx/user/getUserCollectedVenue
"""
@csrf_exempt
def getUserCollectedVenue(request: HttpRequest):
    res = {'data': []}
    data = res['data']
    pageNum = 2  # 一页显示的数量
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)
    openid = request.GET.get("openid")
    longitude = request.GET.get("longitude")
    latitude = request.GET.get("latitude")
    page = int(request.GET.get("page"))  # 获取页码

    venue = openidToCollectedVenue(openid)  # 获取用户收藏的总场馆信息
    # print(venue)

    # 判断有无下一页
    if len(venue) < pageNum*(page-1)+1:
        res['code'] = 0
        res['message'] = "There is no next page"
        res['showAll'] = 1
        return JsonResponse(res)

    venueSortedID = venueDistanceSort(
        venue, latitude, longitude)  # 根据用户与总场馆的距离远近进行排序

    showVenueList(venueSortedID, pageNum, page, res, data)  # 总场馆信息列表展示

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


"""
 @api {get} /wx/user/getUserDiscountCard 获取用户的卡包
 @apiName /user/getUserDiscountCard
 @apiGroup User

 @apiParam {String} openid 用户openid (如：'wx9a3377455576ee6a','wx9a3377455576ee6b')

 @apiSampleRequest /wx/user/getUserDiscountCard
"""
@csrf_exempt
def getUserDiscountCard(request: HttpRequest):
    res = {'data': []}
    data = res['data']
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)
    openid = request.GET.get("openid")
    if openid is None:
        # 新增用户（待写）
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)

    userid = models.User.objects.get(openid=openid).userid
    cardid = models.UserDiscountCard.objects.filter(userid=userid).values(
        'userdiscountcardid', 'discountcardid', 'courtid', 'remainingtimes', 'remainingprice')
    cardid_list = list(cardid)  # queryset转list，便于操作
    # print(cardid_list[0].discountcardid)

    for i in cardid_list:
        discountcardname = models.CourtDiscountCard.objects.get(
            discountcardid=i['discountcardid']).discountcardname  # 从场馆优惠卡表获取优惠卡名
        # print(discountcardname)
        courtname = models.Court.objects.get(courtid=i['courtid']).courtname
        # print(courtname)
        res_card = {'discountcardname': discountcardname, 'courtname': courtname,
                    'remainingtimes': i['remainingtimes'], 'remainingprice': i['remainingprice']}
        data.append(res_card)
        # print(res_card)

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


"""
 @api {get} /wx/user/getOrderSite 获取用户预订的场地
 @apiName /user/getOrderSite
 @apiGroup User

 @apiParam {String} openid 用户openid (如：'wx9a3377455576ee6a','wx9a3377455576ee6b')

 @apiSampleRequest /wx/user/getOrderSite
"""
@csrf_exempt
def getOrderSite(request: HttpRequest):
    res = {'data': []}
    data = res['data']
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)
    openid = request.GET.get("openid")
    if openid is None:
        # 新增用户（待写）
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)

    userid = models.User.objects.get(openid=openid).userid
    order = models.OrderSite.objects.filter(userid=userid).values(
        'siteorderid', 'venueid', 'courtid', 'ordertime', 'orderstateid', 'courttypename', 'originalprice')
    order = list(order)  # queryset转list，便于操作
    print(order)

    for i in order:
        venuename = models.Venue.objects.get(
            venueid=i['venueid']).venuename  # 从场馆优惠卡表获取优惠卡名
        ordertime = i['ordertime'].strftime("%m").lstrip(
            '0')+'月'+i['ordertime'].strftime("%d").lstrip('0')+'日'
        orderChild = models.OrderSiteChild.objects.filter(
            siteorderid=i['siteorderid']).values('sitename')
        print()

        # discountcardname= models.CourtDiscountCard.objects.get(discountcardid=i['discountcardid']).discountcardname#从场馆优惠卡表获取优惠卡名
        # # print(discountcardname)
        # courtname= models.Court.objects.get(courtid=i['courtid']).courtname#从场馆优惠卡表获取优惠卡名
        # # print(courtname)
        res_card = {'venuename': venuename, 'ordertime': ordertime,
                    'courttypename': i['courttypename'], 'originalprice': i['originalprice'], 'sitename': orderChild[0]['sitename']}
        data.append(res_card)
        print(res_card)

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)
