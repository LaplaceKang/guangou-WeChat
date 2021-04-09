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
        openid=openid).values('usercollectedvenue__venueid')
    collectedVenueID = list(collectedVenueID)
    # print(collectedVenueID)

    for i in collectedVenueID:
        # print(i['usercollectedvenue__venueid'])
        if int(venueid) == i['usercollectedvenue__venueid']:
            res['data'] = 1

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


"""
 @api {get} /wx/court/toCollectCourt 收藏这个场馆
 @apiName /Court/toCollectCourt
 @apiGroup Court

 @apiParam {int} venueid 总场馆ID(如：1)
 @apiParam {String} openid 用户openid (如：'wx9a3377455576ee6a','wx9a3377455576ee6b')

 @apiSampleRequest /wx/court/toCollectCourt
"""
@csrf_exempt
def toCollectCourt(request: HttpRequest):
    res = {}
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)
    venueid = request.GET.get("venueid")
    openid = request.GET.get("openid")

    # 获取用户的userid
    userid = models.User.objects.get(
        openid=openid).userid
    # print(userid)

    # 收藏此场馆
    models.UserCollectedVenue.objects.update_or_create(
        userid_id=userid,
        venueid_id=venueid
    )
    
    res['data'] = 1
    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)
