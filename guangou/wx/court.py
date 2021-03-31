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

    court=models.Court.objects.filter(venueid=venueid,courttypeid=courttypeid).values('courtid','specifications','businesstime','courtname')
    print(court)


    # court=list(court)[0] #第一个场馆

    
    for index,item in enumerate(court):
        facilityid=getCourtFacility(item['courtid'])
        res_court = {
        'specifications': item['specifications'], 'facilityid': facilityid,'businesstime':item['businesstime'],'courtname':item['courtname']}
        data.append(res_court)

    
    
    # res['data'] = {'court':data}

    res['code'] = 1
    res['message'] = 'success'
    return JsonResponse(res)
