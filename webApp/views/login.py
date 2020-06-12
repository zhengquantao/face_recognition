from django.shortcuts import render, redirect
from django.http import JsonResponse
from webApp.models import UserInfo
from webApp.util import information, pwd
import uuid


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    salt_password = pwd.hashpwd(password)
    exists = UserInfo.objects.filter(job=username, password=salt_password)
    if not exists:
        return JsonResponse(information.error)
    request.session['user'] = username
    return JsonResponse(information.success)


def logout(request):
    request.session.pop("user")
    return redirect("/login/")