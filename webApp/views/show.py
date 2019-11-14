from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from webApp.util import information
from webApp.models import UserInfo, DateAndWeek, UserAndTitle


class GetDateView(APIView):
    def list(self, request, *args, **kwargs):
        job = request.data.get("username")
        token = request.data.get("token")
        if cache.get(job) != token:
            return Response(information.timeout)

        if UserAndTitle.objects.filter(username__job=job, title__profession="管理员"):
            time_list = DateAndWeek.objects.values("user__job", "user__username", "status", "time").group_by("user__job")
        else:
            time_list = DateAndWeek.objects.filter(user__job=job).values("status", "time")
        return Response(time_list)