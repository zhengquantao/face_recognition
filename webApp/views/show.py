from django.shortcuts import render, redirect
from webApp.util import information, decoration
from webApp.models import UserInfo, DateAndWeek, UserAndTitle
import datetime
from django.db.models import Max, Avg, F, Q, Count


@decoration.login
def show(request):
    job = request.session.get('user')
    if not job:
        return redirect(information.error_path)
    if UserAndTitle.objects.filter(username__job=job, title__profession="管理员"):
        time_list = DateAndWeek.objects.values("user__job", "user__username", "status", "starttime", "endtime")

    else:
        time_list = DateAndWeek.objects.filter(user__job=job).values("status", "starttime", "endtime")
    item = {}
    try:
        for item_obj in time_list:
            # datetime转化时间成字符串
            if item_obj['starttime']:
                starttime = datetime.datetime.strftime(item_obj['starttime'], '%Y-%m-%d %H:%M:%S')
            else:
                starttime = ""
            if item_obj['endtime']:
                endtime = datetime.datetime.strftime(item_obj['endtime'], '%Y-%m-%d %H:%M:%S')
            else:
                endtime = ""
            if item:
                item[item_obj['user__job']].append(
                    [starttime, endtime, item_obj['status'], item_obj['user__username']])
            else:
                item[item_obj['user__job']] = [
                    [starttime, endtime, item_obj['status'], item_obj['user__username']]]
    except:
        pass
    return render(request, "show.html", {"item": item})