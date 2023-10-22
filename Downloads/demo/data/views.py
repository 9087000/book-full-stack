from optparse import Values
from typing_extensions import Self
from django.shortcuts import render
from rest_framework.decorators import api_view
from . models import projectdemo
from rest_framework.response import Response as RestResponse
from django.http import JsonResponse
from demo import commanResponse
from data import service
from django.db.models import Q

# Create your views here.

@api_view(['POST'])
def show(request):
    dict_data = {}
    task = []
    data = projectdemo.objects.all().values('roll_no','marks','strength')
    print(data) 
    for temp in data:
        for k,v in temp.items():
            if k not in dict_data.keys():
                dict_data[k] = [v]
            else:
                dict_data[k].append(v)
    print(dict_data)
                
    # dict_data['roll_no']=data
    # data1 = projectdemo.objects.all().values('B')
    # data2 = projectdemo.objects.all().values('C')
    return JsonResponse(commanResponse.Response.sendsuccessResponse(None, dict_data, "Success"), safe = False)

@api_view(['POST'])
def calculate(request):
    roll_no = request.data['roll_no']
    marks = request.data['marks']
    strength = request.data['strength']
    data_tem = projectdemo.objects.filter(roll_no =roll_no).filter(marks=marks).filter(strength=strength).values()
    if data_tem.exists():
        data = service.sumres().summ(roll_no,marks,strength,request)
        return JsonResponse(commanResponse.Response.sendsuccessResponse(None,data, "Success"), safe = False)
    
    return JsonResponse(commanResponse.Response.senderrorResponse(None,[],'data not in the table'),safe = False,status=500)


    
    
    
    # print(data_tem)
    # if data_tem.exists():
    #     data = service.sumres().summ(roll_no,marks,strength,request)
    #     return JsonResponse(commanResponse.Response.sendsuccessResponse(None,data, "Success"), safe = False)
  
    # return JsonResponse(commanResponse.Response.senderrorResponse(None,[],'data not in the table'),safe = False,status=500)






