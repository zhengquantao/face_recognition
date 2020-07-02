from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from webApp.util import information
from webApp.util.face import Face
from webApp.models import DateAndWeek, UserInfo
import datetime
import os
import base64
import array



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
    # 普通模式========= 挺慢
    # score, job = Face.score(img_path)
    # ============== 数据库形式 ===============
    import time
    images_list = UserInfo.objects.filter(~Q(image_content=None)).values("image_content", "uid")
    face_data = Face.face_detection(img_path)
    score = 1
    for item in images_list:
        try:
            score = Face.compare(face_data, eval(item['image_content']))
            if score < 0.4:
                user = item['uid']
                break
        except:
             pass
            # return JsonResponse(information.play_error)
    # =========================================
    if score < 0.4:
        time = datetime.datetime.now()
        # 早上时间打卡
        if information.morning[0] < time.hour < information.morning[1]:
            is_get = DateAndWeek.objects.filter(user__uid=user, starttime__year=time.year,
                                       starttime__month=time.month, starttime__day=time.day)
            if is_get:
                return JsonResponse(information.play_exits)
            if information.morning[0]+1 <= time.hour < information.morning[1]:
                DateAndWeek.objects.create(user__uid=user, starttime=time, status="已迟到")
            else:
                DateAndWeek.objects.create(user__uid=user, starttime=time, status="已签到")
            return JsonResponse(information.play_success)
        # 下午时间打卡
        elif information.after[0] < time.hour < information.after[1]:
            DateAndWeek.objects.filter(user__uid=user, starttime__year=time.year,
                                       starttime__month=time.month, starttime__day=time.day).update(endtime=time)
            return JsonResponse(information.play_back)
        else:
            return JsonResponse(information.play_error)

    return JsonResponse(information.play_error)


def add(request):
    job = request.session.get("user")
    if request.method == "GET":
        return render(request, "add.html")

    images = request.POST.get("img")
    if not job:
        return JsonResponse(information.timeout)
    if not images:
        return JsonResponse(information.play_error)
    is_image = UserInfo.objects.filter(job=job).values("image", "image_content").first()
    if is_image['image']:
        return JsonResponse(information.is_image)
    img = base64.b64decode(images.split(',')[1])
    img_path = os.path.join("faces", job+'.png')
    with open(img_path, 'wb') as f:
        f.write(img)
        f.close()
    content = Face.face_detection(img_path)
    UserInfo.objects.filter(job=job).update(image=img_path, image_content=list(content))
    return JsonResponse(information.record_success)