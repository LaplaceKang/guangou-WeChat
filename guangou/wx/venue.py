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
    pageNum = 4  # 一页显示的数量
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

    venue = models.Venue.objects.filter(cityid_id=cityid).values(
        'venueid', 'longitude', 'latitude')  # 筛选符合城市ID的总场馆

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

    showVenueList(venueSortedID, pageNum, page, res, data)  # 总场馆信息列表展示

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

    courtType = models.VenueCityCourtType.objects.filter(
        cityid_id=cityid).values('courttypeid')  # 筛选符合城市ID的总场馆
    courtType = list(courtType)  # queryset转list，便于操作
    # print(courtType)

    # for i in courtType:
    #     i['courttypename'] = Map_CourtType[i['courttypeid']]
    #     data.append(i)
    res['data'] = courtType
    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


"""
 @api {get} /wx/venue/filterCourtType 根据总场馆的运动类型筛选总场馆
 @apiName /venue/filterCourtType
 @apiGroup Venue

 @apiParam {int} courttypeid 运动类型ID（如：1）
 @apiParam {int} cityid 用户所在城市ID（如：1）
 @apiParam {decimal} longitude 用户所在位置的经度(如：116.346352)
 @apiParam {decimal} latitude  用户所在位置的纬度(如：39.960501)
 @apiParam {int} page  页码

 @apiSampleRequest /wx/venue/filterCourtType
"""
@csrf_exempt
def filterCourtType(request: HttpRequest):
    res = {'data': []}
    data = res['data']
    pageNum = 4  # 一页显示的数量
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)

    courttypeid = request.GET.get("courttypeid")
    cityid = request.GET.get("cityid")
    longitude = request.GET.get("longitude")
    latitude = request.GET.get("latitude")
    page = int(request.GET.get("page"))  # 获取页码
    if not courttypeid:
        res['code'] = 0
        res['message'] = "Please enter the courttypeid"
        return JsonResponse(res)

    venueidList = models.VenueCourtType.objects.filter(
        courttypeid_id=courttypeid).values('venueid')  # 根据场馆运动类型id筛选出总场馆
    venueidList = list(venueidList)

    # 判断有无下一页
    if len(venueidList) < pageNum*(page-1)+1:
        res['code'] = 0
        res['message'] = "There is no next page"
        res['showAll'] = 1
        return JsonResponse(res)

    venue = []
    for i in venueidList:
        oneVenue = models.Venue.objects.filter(venueid=i['venueid'],
                                               cityid_id=cityid).values('venueid', 'longitude', 'latitude', 'venuename', 'addressshort')
        if oneVenue:  # 如果这个总场馆在这个城市
            oneVenue = list(oneVenue)
            venue.append(oneVenue[0])

    venueSort = venueDistanceSort(venue, latitude, longitude)  # 按距离排序
    print(venueSort)

    res['showAll'] = 0  # 默认没有显示完
    for index in range(pageNum*(page-1), pageNum*page):
        if index > len(venueSort)-1:  # 如果查询的数量超过已有数量
            res['showAll'] = 1
            break
        i = venueSort[index]
        courttype = VenueCourtType(i['venueid'])  # 获取总场馆运动类型
        res_venue = {'venueid': i['venueid'], 'venuename': i['venuename'], 'addressshort': i['addressshort'],
                     'longitude': i['longitude'], 'latitude': i['latitude'], 'distance': str(round(i['distance']))+'m', 'courttype': courttype}
        lowestprice = venueidToLowestPrice(i['venueid'])  # 获取最低价格
        res_venue['lowestprice'] = lowestprice
        # print(res_venue)
        data.append(res_venue)

    # for i in venueSort:  # 展示信息
    #     courttype = VenueCourtType(i['venueid'])  # 获取总场馆运动类型
    #     res_venue = {'venueid': i['venueid'], 'venuename': i['venuename'], 'addressshort': i['addressshort'],
    #                  'longitude': i['longitude'], 'latitude': i['latitude'], 'distance': str(round(i['distance']))+'m', 'courttype': courttype}
    #     lowestprice = venueidToLowestPrice(i['venueid'])  # 获取最低价格
    #     res_venue['lowestprice'] = lowestprice
    #     # print(res_venue)
    #     data.append(res_venue)

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


"""
 @api {get} /wx/venue/getVenueDetail 根据总场馆id获取其具体信息
 @apiName /venue/getVenueDetail
 @apiGroup Venue

 @apiParam {int} venueid 总场馆ID(如：1)

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

    # venue=models.Venue.objects.filter(venueid=venueid).values('information','address','phonenumber')
    # venue=list(venue)
    venue = models.Venue.objects.get(venueid=venueid)
    # print(venue.information)

    # res_court=getCourtDetail(court['courtid'])
    # models.CourtDiscountCard.objects.filter(courtid=court['courtid']).values('discountcardname','specifications')
    # facility=models.CourtCourtFacility.objects.filter(courtid=court['courtid']).values('facilityid')
    # facility=list(facility) #场馆设施ID，具体名称在Map中查找
    # facilityid=[]
    # for i in facility:
    #     facilityid.append(i['facilityid'])

    res_venue = {'information': venue.information,
                 'address': venue.address, 'phonenumber': venue.phonenumber, }

    # print(facility)
    res['data'] = {'venue': res_venue}

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


"""
 @api {get} /wx/venue/searchVenue 搜索总场馆
 @apiName /venue/searchVenue
 @apiGroup Venue

 @apiParam {string} searchName 搜索的总场馆名称
 @apiParam {int} cityid 用户所在城市ID(如：1)
 @apiParam {decimal} longitude 用户所在位置的经度(如：116.346352)
 @apiParam {decimal} latitude  用户所在位置的纬度(如：39.960501)
 @apiParam {int} courttypeid 运动类型ID（如：1）
 @apiParam {int} page  页码

 @apiSampleRequest /wx/venue/searchVenue
"""
@csrf_exempt
def searchVenue(request: HttpRequest):
    res = {'data': []}
    data = res['data']
    pageNum = 4  # 一页显示的数量
    if request.method != 'GET':
        res['code'] = 0
        res['message'] = "bad request"
        return JsonResponse(res)

    searchName = request.GET.get("searchName")
    courttypeid = request.GET.get("courttypeid")
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

    # venue = models.Venue.objects.filter(
    #     venuename__contains=searchName,cityid=cityid).values("venueid", 'longitude', 'latitude')
    venue = models.VenueCourtType.objects.filter(
        venueid__venuename__contains=searchName, venueid__cdcityid=cityid, courttypeid=courttypeid).values("venueid", 'longitude', 'latitude')


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

    showVenueList(venueSortedID, pageNum, page, res, data)  # 总场馆信息列表展示

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)


# def getCourtFacility(request: HttpRequest):
#     res = {'data': []}
#     if request.method != 'GET':
#         res['code'] = 0
#         res['message'] = "bad request"
#         return JsonResponse(res)
#     courtid = request.GET.get("courtid")

#     facility=models.CourtCourtFacility.objects.filter(courtid=courtid).values("facilityid")
#     facility=list(facility)
#     # print(facility)
#     res['data']=facility

#     res['code'] = 1
#     res['message'] = 'success'
#     return JsonResponse(res)
