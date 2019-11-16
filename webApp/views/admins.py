from django.core.cache import cache
from django.shortcuts import render, Http404
from django.http import JsonResponse
from webApp.util import information
from webApp.models import UserInfo, DateAndWeek


def admin(request):
    job = request.data.get("username")
    token = request.data.get("token")
    if cache.get(job) != token:
        return Http404(information.timeout)
    time_list = DateAndWeek.objects.filter(user__job=job).values("status", "time")
    return render(request, "admin.html", time_list)