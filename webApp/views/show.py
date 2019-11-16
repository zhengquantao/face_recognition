from django.shortcuts import render, Http404
from webApp.util import information, decoration
from webApp.models import UserInfo, DateAndWeek, UserAndTitle


@decoration.login
def show(request):
    job = request.session.get('user')
    if job:
        return Http404(information.timeout)
    if UserAndTitle.objects.filter(username__job=job, title__profession="管理员"):
        time_list = DateAndWeek.objects.values("user__job", "user__username", "status", "time").group_by("user__job")
    else:
        time_list = DateAndWeek.objects.filter(user__job=job).values("status", "time")
    return render(request, "show.html", time_list)