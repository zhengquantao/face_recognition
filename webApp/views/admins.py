from django.shortcuts import render, redirect
from django.http import JsonResponse
from webApp.util import information, decoration, pwd
from webApp.models import UserInfo, DateAndWeek, UserAndTitle, Title


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


@decoration.login
def add_person(request):
    if request.method == "GET":
        job = request.session.get("user")
        is_user = UserAndTitle.objects.filter(username__job=job, title__profession="管理员")
        if not is_user:
            return redirect(information.error_path)
        return render(request, "add_person.html")
    username = request.POST.get("username")
    job = request.POST.get("job")
    email = request.POST.get("email")
    profession = request.POST.get("profession")
    password = request.POST.get("password")
    hash_password = pwd.hashpwd(password)
    try:
        UserInfo.objects.create(username=username, job=job, email=email, password=hash_password)
        user = UserInfo.objects.filter(job=job).first()
        title = Title.objects.filter(profession=profession)
        if not title:
            Title.objects.create(profession=profession)
            title = Title.objects.filter(profession=profession)
        UserAndTitle.objects.create(username=user, title=title.first())
    except:
        return JsonResponse(information.timeout)
    return JsonResponse(information.add_success)