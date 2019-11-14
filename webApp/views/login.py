from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from webApp.models import UserInfo
from webApp.util import information, pwd
import uuid


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        salt_password = pwd.hashpwd(password)
        exists = UserInfo.objects.filter(job=username, password=salt_password)
        if not exists:
            return Response(information.error)
        cache.set(username, uuid.uuid4(), 60*60*6)
        return Response(information.success)
