# 获取数据库数据的方法
from wx import models
from geopy.distance import geodesic
from wx.util.typeMap import *
import math

# '''
# 获取总场馆展示列表信息
# venueID：包含总场馆venueid的List
# cityid：城市id
# data：要返回的json数据里的data字段
# '''


# def getVenueList(venueID, cityid, data):
#     for i in venueID:
#         venue = models.Venue.objects.get(
#             venueid=i['venueid'], cityid=cityid)  # 从数据库获取总场馆
#         console.log(venue)
#         courttypeid = models.VenueCourtType.objects.filter(
#             venueid=i['venueid']).values('courttypeid')  # 总场馆的运动类型
#         courttype = []
#         for j in list(courttypeid):
#             courttype.append(Map_CourtType[j['courttypeid']])  # 将所有运动类型放入数组中
#         res_venue = {'venueid': venue.venueid, 'venuename': venue.venuename, 'addressshort': venue.addressshort,
#                      'longitude': venue.longitude, 'latitude': venue.latitude, 'courttype': courttype}
#         lowestprice = models.Court.objects.filter(venueid=i['venueid']).order_by(
#             'lowestprice').first().lowestprice  # 去子场馆找出最低价格
#         res_venue['lowestprice'] = lowestprice
#         # print(lowestprice)
#         data.append(res_venue)
#         # print(res_venue)


'''
根据用户与总场馆的距离远近进行排序
venue：包含总场馆经纬度信息的List
latitude,longitude：用户所在地点的经纬度
'''


def venueDistanceSort(venue, latitude, longitude):
    for i in venue:
        distance = geodesic(
            (i['latitude'], i['longitude']), (latitude, longitude)).m  # 计算用户与总场馆之间距离
        i['distance'] = distance
    venueSortedID = sorted(venue, key=lambda x: x['distance'])  # 按距离远近对总场馆排序
    return venueSortedID


'''
根据城市id筛选出总场馆
'''


def cityToVenue(cityid):
    cityid_FK = models.VenueCity.objects.get(cityid=cityid)  # 获取VenueCity的外键
    venue = models.Venue.objects.filter(cityid=cityid_FK).values(
        'venueid', 'longitude', 'latitude')  # 筛选符合城市ID的总场馆
    return list(venue)  # queryset转list，便于操作


'''
根据场馆运动类型id筛选出总场馆
'''


def courtTypeToVenue(courttypeid):
    courttypeid_FK = models.CourtType.objects.get(
        courttypeid=courttypeid)  # 获取VenueCity的外键
    venueid = models.VenueCourtType.objects.filter(
        courttypeid=courttypeid_FK).values('venueid')  # 筛选符合运动类型的总场馆
    return list(venueid)  # queryset转list，便于操作


'''
根据总场馆id得到总场馆信息（venueid, longitude, latitude）
venueID：存储总场馆id的列表
'''


def venueidToVenue(venueID):
    venue = []
    for i in venueID:
        venueOne = models.Venue.objects.filter(
            venueid=i['venueid']).values(
            'venueid', 'longitude', 'latitude')    # 从数据库获取总场馆
        venueOne = list(venueOne)  # queryset转list，便于操作
        # print(venueOne[0])
        venue.append(venueOne[0])
    return venue


'''
获取总场馆运动类型
venueid:总场馆的venueid
'''


def VenueCourtType(venueid):
    courttypeid = models.VenueCourtType.objects.filter(
        venueid=venueid).values('courttypeid')  # 总场馆的运动类型
    courttype = []
    for j in list(courttypeid):
        courttypeOne = {'courttypeid': j['courttypeid'],
                        'courttypename': Map_CourtType[j['courttypeid']]}
        courttype.append(courttypeOne)  # 将所有运动类型放入数组中
    return courttype


'''
根据用户openid获取用户收藏的总场馆信息(venueid, longitude, latitude)
'''


def openidToCollectedVenue(openid):
    userid = models.User.objects.get(openid=openid).userid
    venueID = models.UserCollectedVenue.objects.filter(
        userid=userid).values('venueid')  # 用户收藏的总场馆id
    # 根据总场馆id得到总场馆信息（venueid, longitude, latitude）
    venue = venueidToVenue(venueID)
    return venue


'''
根据总场馆id获取最低价格
'''


def venueidToLowestPrice(venueid):
    try:
        lowestprice = models.Court.objects.filter(venueid=venueid).order_by(
            'lowestprice').first().lowestprice  # 去子场馆找出最低价格
    except AttributeError:
        lowestprice = ''  # 有的场馆还没设置价格
        return lowestprice
    else:
        return math.floor(lowestprice)


'''
总场馆信息列表展示
'''


def showVenueList(venueSortedID, pageNum, page, res, data):
    res['showAll'] = 0
    for index in range(pageNum*(page-1), pageNum*page):
        if index > len(venueSortedID)-1:  # 如果查询的数量超过已有数量
            res['showAll'] = 1
            break
        venueInf = models.Venue.objects.get(
            venueid=venueSortedID[index]['venueid'])  # 从数据库获取总场馆信息
        courttype = VenueCourtType(venueInf.venueid)  # 获取总场馆运动类型
        res_venue = {'venueid': venueInf.venueid, 'venuename': venueInf.venuename,
                     'addressshort': venueInf.addressshort, 'longitude': venueInf.longitude, 'latitude': venueInf.latitude, 'courttype': courttype}
        res_distance = venueSortedID[index]['distance']  # 场馆距离
        if res_distance < 1000:  # 小于1000m
            res_venue['distance'] = str(round(res_distance))+'m'
        elif res_distance < 10000:  # 保留一位小数
            res_venue['distance'] = str(round(res_distance/1000, 1))+'km'
        else:  # 取整
            res_venue['distance'] = str(round(res_distance/1000))+'km'
        lowestprice = venueidToLowestPrice(venueInf.venueid)  # 获取最低价格
        res_venue['lowestprice'] = lowestprice
        data.append(res_venue)


"""
 根据场馆id获取场馆设施
 courtid 场馆id(如：2)
"""


def getCourtFacility(courtid):
    facility = models.CourtCourtFacility.objects.filter(
        courtid=courtid).values('facilityid')
    facility = list(facility)  # 场馆设施ID，具体名称在Map中查找
    facilityid = []
    for i in facility:
        facilityid.append(i['facilityid'])
    return facilityid
