from django.shortcuts import render, redirect
from django.http import JsonResponse
from webApp.models import DateAndWeek, UserInfo
import datetime, time


def add_text(request):
    # item = DateAndWeek.objects.filter(id__gt=57
    #                                   ).values("starttime")
    # for i in item:
    #     print(i['starttime'])
    # timeStamp = 1580545299+86400*7
    # dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    # print(dateArray)
    timeStamp = 1580545299
    user_obj = UserInfo.objects.get(job=2016032524)
    for i in range(10):
        timeStamp = timeStamp+86400
        dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
        time.sleep(0.4)
        DateAndWeek.objects.create(user=user_obj, starttime=dateArray, status="已签到")
        print("OK--------")

    return JsonResponse({"K": ''})