from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple
import json

# Create your views here.
from django.http import HttpResponse, JsonResponse


@csrf_exempt
def getTemparatureData(request):
    # if request.method == 'POST':
    #     name = request.POST["name"]
    #     address = request.POST["address"]
    #     phone = request.POST["phone"]
    #     password = request.POST["password"]

    #     with connection.cursor() as cursor_1:
    #         cursor_1.execute("INSERT INTO homeowner(name,address,phone,password) VALUES ('"+str(
    #             name) + "' ,'"+str(address) + "','"+str(phone) + "','"+str(password) + "' )")
    #         #row1 = cursor_1.fetchall()
    #         # print(row1)
    #         #data = "Success"
    #         data = {"message": "Success"}
    #         return JsonResponse(data)
    return HttpResponse("Hello, world. You're at the polls index.")