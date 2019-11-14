from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from webApp.util import information
from webApp.models import UserInfo, DateAndWeek


class AdminView(APIView):
    def all(self, request, *args, **kwargs):
        job = request.data.get("username")
        token = request.data.get("token")
        if cache.get(job) != token:
            return Response(information.timeout)
        time_list = DateAndWeek.objects.filter(user__job=job).values("status", "time")
        return Response(time_list)