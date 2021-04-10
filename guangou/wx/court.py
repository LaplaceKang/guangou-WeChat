from django.shortcuts import render, HttpResponse
from wx import models
from django.views.decorators.csrf import csrf_exempt
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from wx.util.db import *

"""
 @api {get} /wx/court/getCourtDetail 根据总场馆id与运动类型id获取其具体信息
 @apiName /Court/getCourtDetail
 @apiGroup Court

 @apiParam {int} venueid 总场馆ID(如：1)
 @apiParam {int} courttypeid 运动类型ID

 @apiSampleRequest /wx/court/getCourtDetail
"""
@csrf_exempt
def getCourtDetail(request: HttpRequest):
    res = {'data': []}
    data = res['data']
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)
    venueid = request.GET.get("venueid")
    courttypeid = request.GET.get("courttypeid")

    court = models.Court.objects.filter(venueid=venueid, courttypeid=courttypeid).values(
        'courtid', 'specifications', 'businesstime', 'courtname')
    # print(court)

    for index, item in enumerate(court):
        facilityid = getCourtFacility(item['courtid'])
        discountcardtypename = getcourtDiscountCardTypeInf(item['courtid'])
        res_court = {
            'specifications': item['specifications'], 'facilityid': facilityid, 'businesstime': item['businesstime'], 'courtname': item['courtname'], 'discountcardtypename': discountcardtypename}
        data.append(res_court)
    # res['data'] = {'court':data}

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


"""
 @api {get} /wx/court/isCourtCollected 该场馆是否被用户收藏
 @apiName /Court/isCourtCollected
 @apiGroup Court

 @apiParam {int} venueid 总场馆ID(如：1)
 @apiParam {String} openid 用户openid (如：'wx9a3377455576ee6a','wx9a3377455576ee6b')

 @apiSampleRequest /wx/court/isCourtCollected
"""
@csrf_exempt
def isCourtCollected(request: HttpRequest):
    res = {}
    # data = res['data']
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)
    venueid = request.GET.get("venueid")
    openid = request.GET.get("openid")

    collectedVenueID = models.User.objects.filter(
        openid=openid).values('usercollectedvenue__venueid', 'usercollectedvenue__isdeleted')
    collectedVenueID = list(collectedVenueID)
    # print(collectedVenueID)

    res['data'] = False
    for i in collectedVenueID:
        # print(i['usercollectedvenue__venueid'])
        if int(venueid) == i['usercollectedvenue__venueid'] and i['usercollectedvenue__isdeleted'] == False:
            res['data'] = True

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


"""
 @api {get} /wx/court/changeCollectCourt 改变场馆的收藏状态
 @apiName /Court/changeCollectCourt
 @apiGroup Court

 @apiParam {int} venueid 总场馆ID(如：1)
 @apiParam {String} openid 用户openid (如：'wx9a3377455576ee6a','wx9a3377455576ee6b')

 @apiSampleRequest /wx/court/changeCollectCourt
"""
@csrf_exempt
def changeCollectCourt(request: HttpRequest):
    res = {}
    # data = res['data']
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)
    venueid = request.GET.get("venueid")
    openid = request.GET.get("openid")

    userid = models.User.objects.filter(openid=openid).values(
        'usercollectedvenue__venueid', 'usercollectedvenue__isdeleted', 'userid')
    userid = list(userid)
    # print(userid)

    # 若用户之前已收藏过，则将删除标志取反（即改变收藏状态）
    for i in userid:
        if i['usercollectedvenue__venueid'] == int(venueid):
            # print(i['usercollectedvenue__isdeleted'])
            if i['usercollectedvenue__isdeleted']:
                models.UserCollectedVenue.objects.filter(userid=i['userid'], venueid=venueid).update(
                    isdeleted=False
                )
                res['isCollected'] = True
                res['code'] = 1
                res['message'] = 'success'
                return JsonResponse(res)
            else:
                models.UserCollectedVenue.objects.filter(userid=i['userid'], venueid=venueid).update(
                    isdeleted=True
                )
                res['isCollected'] = False
                res['code'] = 1
                res['message'] = 'success'
                return JsonResponse(res)
        else:
            pass

    # 若用户之前没收藏过，则收藏
    models.UserCollectedVenue.objects.update_or_create(
        userid_id=userid[0]['userid'],
        venueid_id=venueid,
        isdeleted=False
    )
    res['isCollected'] = True

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)
