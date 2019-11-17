from django.core.cache import cache
from django.shortcuts import render, redirect
from django.http import JsonResponse
from webApp.util import information, decoration
from webApp.models import UserInfo, DateAndWeek, UserAndTitle


@decoration.login
def admin(request):
    job = request.session.get("user")
    if not job:
        return redirect(information.error_path)
    time_list = DateAndWeek.objects.filter(user__job=job).values("status", "strattime", "endtime")
    return render(request, "admin.html", {"time_list": time_list})


@decoration.login
def person(request):
    job = request.session.get("user")
    if not job:
        return redirect(information.error_path)
    msg = UserAndTitle.objects.filter(username__job=job).values("username__job", "username__email", "username__image",
                                                                "username__username", "title__profession")
    return render(request, "person.html", {"msg": msg[0]})