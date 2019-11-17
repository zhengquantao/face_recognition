from django.shortcuts import render, redirect
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
                user_obj = UserInfo.objects.get(image="faces/"+job)
                # 早上时间打卡
                if 7 < time.hour < 9:
                    DateAndWeek.objects.create(user=user_obj, starttime=time, status="已签到")
                    return JsonResponse(information.play_success)
                # 下午时间打卡
                elif 17 < time.hour < 20:
                    DateAndWeek.objects.filter(user__job=job, starttime__year=time.year,
                                               starttime__month=time.month, starttime__day=time.day).update(endtime=time)

                    return JsonResponse(information.play_success)

                else:
                    return JsonResponse(information.play_error)
    return JsonResponse(information.play_error)


def add(request):
    job = request.session.get("user")
    if request.method == "GET":
        is_image = UserInfo.objects.filter(job=job).values("image")
        if not is_image:
            return redirect(information.error_path)
        return render(request, "add.html")

    images = request.POST.get("img")
    if not job:
        return JsonResponse(information.timeout)
    if not images:
        return JsonResponse(information.play_error)
    img = base64.b64decode(images.split(',')[1])
    img_path = os.path.join("faces", job+'.png')
    with open(img_path, 'wb') as m:
        m.write(img)
        m.close()
    UserInfo.objects.filter(job=job).update(image=img_path)
    return JsonResponse(information.record_success)