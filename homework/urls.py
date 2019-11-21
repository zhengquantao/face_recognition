"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from webApp.views import login, show, admins, face, error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login.login),
    path('list/', show.show),
    path('admins/', admins.admin),
    path('face/', face.face),
    path('add/', face.add),
    path('error/', error.error),
    path('logout/', login.logout),
    path('person/', admins.person),
    path('insert/', admins.add_person),
    path('delete/', admins.delete),
    path('', face.home)
]
