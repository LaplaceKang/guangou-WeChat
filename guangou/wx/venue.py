from django.shortcuts import render, HttpResponse
from wx import models
from django.views.decorators.csrf import csrf_exempt
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from wx.util.typeMap import *
from wx.util.db import *

"""
 @api {get} /wx/venue/getIndexVenue 获取主页展示的总场馆
 @apiName /venue/getIndexVenue
 @apiGroup Venue

 @apiParam {int} cityid 用户所在城市ID(如：1)
 @apiParam {decimal} longitude 用户所在位置的经度(如：116.346352)
 @apiParam {decimal} latitude  用户所在位置的纬度(如：39.960501)
 @apiParam {int} page  页码

 @apiSampleRequest /wx/venue/getIndexVenue
"""
@csrf_exempt
def getIndexVenue(request: HttpRequest):
    res = {'data': []}
    data = res['data']
    pageNum = 2  # 一页显示的数量
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)

    cityid = request.GET.get("cityid")
    longitude = request.GET.get("longitude")
    latitude = request.GET.get("latitude")
    page = int(request.GET.get("page"))  # 获取页码
    if not(longitude or latitude or cityid):
        res['code'] = 0
        res['message'] = "Please enter the parameters"
        return JsonResponse(res)
    if page < 0:
        res['code'] = 0
        res['message'] = "Page Error"
        return JsonResponse(res)

    venue = cityToVenue(cityid)  # 根据城市id筛选出总场馆

    # 判断有无下一页
    if len(venue) < pageNum*(page-1)+1:
        res['code'] = 0
        res['message'] = "There is no next page"
        res['showAll'] = 1
        return JsonResponse(res)

    # print(venue)

    venueSortedID = venueDistanceSort(
        venue, latitude, longitude)  # 根据用户与总场馆的距离远近进行排序

    # print(venueSortedID)

    
    showVenueList(venueSortedID,pageNum,page,res,data)#总场馆信息列表展示

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


"""
 @api {get} /wx/venue/getCourtType 获取主页展示的场馆类型
 @apiName /venue/getCourtType
 @apiGroup Venue

 @apiParam {int} cityid 用户所在城市ID

 @apiSampleRequest /wx/venue/getCourtType
"""
@csrf_exempt
def getCourtType(request: HttpRequest):
    res = {'data': []}
    data = res['data']
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)

    cityid = request.GET.get("cityid")
    if not cityid:
        res['code'] = 0
        res['message'] = "Please enter the cityid"
        return JsonResponse(res)
    cityid_FK = models.VenueCity.objects.get(cityid=cityid)  # 获取cityid这个外键
    courtType = models.VenueCityCourtType.objects.filter(
        cityid=cityid_FK).values('courttypeid')  # 筛选符合城市ID的总场馆
    courtType = list(courtType)  # queryset转list，便于操作
    # print(courtType)

    for i in courtType:
        i['courttypename'] = Map_CourtType[i['courttypeid']]
        data.append(i)

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


"""
 @api {get} /wx/venue/filterCourtType 根据总场馆的运动类型筛选总场馆
 @apiName /venue/filterCourtType
 @apiGroup Venue

 @apiParam {int} courttypeid 运动类型ID
 @apiParam {int} cityid 用户所在城市ID
 @apiParam {decimal} longitude 用户所在位置的经度
 @apiParam {decimal} latitude  用户所在位置的纬度

 @apiSampleRequest /wx/venue/filterCourtType
"""
@csrf_exempt
def filterCourtType(request: HttpRequest):
    res = {'data': []}
    data = res['data']
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)

    courttypeid = request.GET.get("courttypeid")
    cityid = request.GET.get("cityid")
    longitude = request.GET.get("longitude")
    latitude = request.GET.get("latitude")
    if not courttypeid:
        res['code'] = 0
        res['message'] = "Please enter the courttypeid"
        return JsonResponse(res)

    venueidList = courtTypeToVenue(courttypeid)  # 根据场馆运动类型id筛选出总场馆

    venue = []
    for i in venueidList:
        cityid_FK = models.VenueCity.objects.get(cityid=cityid)  # 获取cityid这个外键
        oneVenue = models.Venue.objects.filter(venueid=i['venueid'],
                                               cityid=cityid_FK).values('venueid', 'longitude', 'latitude', 'venuename', 'addressshort')
        if oneVenue: #如果这个总场馆在这个城市
            oneVenue=list(oneVenue)
            venue.append(oneVenue[0])

    venueSort=venueDistanceSort(venue, latitude, longitude)
    print(venueSort)
    for i in venueSort:
        courttype=VenueCourtType(i['venueid']) #获取总场馆运动类型
        res_venue = {'venueid': i['venueid'], 'venuename': i['venuename'], 'addressshort': i['addressshort'],
                     'longitude': i['longitude'], 'latitude': i['latitude'],'distance': str(round(i['distance']))+'m', 'courttype': courttype}
        lowestprice=venueidToLowestPrice(i['venueid'])#获取最低价格
        res_venue['lowestprice'] = lowestprice
        # print(res_venue)
        data.append(res_venue)

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)

"""
 @api {get} /wx/venue/getVenueDetail 根据总场馆id获取其具体信息
 @apiName /venue/getVenueDetail
 @apiGroup Venue

 @apiParam {int} venueid 总场馆ID(如：1)
 @apiParam {int} courttypeid 运动类型ID

 @apiSampleRequest /wx/venue/getVenueDetail
"""
@csrf_exempt
def getVenueDetail(request: HttpRequest):
    res = {'data': []}
    data = res['data']
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)
    venueid = request.GET.get("venueid")
    courttypeid = request.GET.get("courttypeid")

    # venue=models.Venue.objects.filter(venueid=venueid).values('information','address','phonenumber')
    # venue=list(venue)
    venue=models.Venue.objects.get(venueid=venueid)
    # print(venue.information)

    court=models.Court.objects.filter(venueid=venueid,courttypeid=courttypeid).values('courtid','specifications')
    court=list(court)[0]
    # print(court)

    # models.CourtDiscountCard.objects.filter(courtid=court['courtid']).values('discountcardname','specifications')
    facilityid=models.CourtCourtFacility.objects.filter(courtid=court['courtid']).values('facilityid')
    facilityid=list(facilityid)
    # print(facility)
    facility=[]
    for i in facilityid:
        facilityOne=models.CourtFacility.objects.filter(facilityid=i['facilityid']).values('facilityname','facilityicon')
        facility.append(list(facilityOne)[0])

    # print(facility)
    res['data'] = {'information': venue.information, 'address': venue.address, 'phonenumber': venue.phonenumber,'specifications':court['specifications'],'facility':facility}


    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)