from django.shortcuts import render
from django.http import JsonResponse
from webApp.util import information
from webApp.util.face import Face
from webApp.models import DateAndWeek, UserInfo
import datetime
import os
import base64


def home(request):
    return render(request, 'face.html')


def face(request):
    images = request.POST.get("img")
    if not images:
        return JsonResponse(information.play_error)
    img = base64.b64decode(images.split(',')[1])
    img_path = os.path.join("static", "images", "test.png")
    with open(img_path, 'wb') as m:
        m.write(img)
        m.close()
    for parent, dirnames, filenames in os.walk(os.path.join("faces")):
        for job in filenames:
            score = Face.score(os.path.join("faces", job), img_path)
            if score < 0.5:
                time = datetime.datetime.now()
                user = UserInfo.objects.filter(job=job).fisrt()
                # 早上时间打卡
                if 7 < time.hour < 9:
                    DateAndWeek.objects.create(user=user, starttime=time)
                    return JsonResponse(information.play_success)
                # 下午时间打卡
                elif 17 < time.hour < 20:
                    DateAndWeek.objects.filter(user__job=job, starttime__year=time.year,
                                               starttime__month=time.month, starttime__day=time.day).update(endtime=time)

                    return JsonResponse(information.play_success)

                else:
                    return JsonResponse(information.play_error)
    return JsonResponse(information.play_error)
