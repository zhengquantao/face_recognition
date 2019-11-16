from django.shortcuts import render, redirect
from webApp.util import information, decoration
from webApp.models import UserInfo, DateAndWeek, UserAndTitle


@decoration.login
def show(request):
    job = request.session.get('user')
    if not job:
        return redirect(information.error_path)
    if UserAndTitle.objects.filter(username__job=job, title__profession="管理员"):
        time_list = DateAndWeek.objects.values("user__job", "user__username", "status", "starttime", "endtime").group_by("user__job")
    else:
        time_list = DateAndWeek.objects.filter(user__job=job).values("status", "starttime", "endtime")
    return render(request, "show.html", {"time_list": time_list})