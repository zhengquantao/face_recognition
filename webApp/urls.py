from django.urls import path
from webApp.views import login, show, admin

urlpatterns = [
    path('login$', login.LoginView.as_view()),
    path('list$', show.GetDateView.as_view({'get': 'list'})),
    path('admin$', admin.AdminView.as_view({'get': 'all'}))
]
