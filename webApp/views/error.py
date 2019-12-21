from django.shortcuts import render


def error(request):
    return render(request, "error.html")