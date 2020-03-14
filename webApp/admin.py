from django.contrib import admin
from webApp.models import UserInfo, UserAndTitle, Title, DateAndWeek


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['uid', 'job', 'username', 'image', 'password', 'email']
    # list_editable = ['uid', 'job', 'username', 'image', 'password', 'email']


class DateAndWeekAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ['user', 'starttime', 'endtime',  'status']
    search_fields = ['user', 'starttime', 'endtime',  'status']


class UserAndTitleAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ['id', 'username', 'title']
    # list_editable = ['id', 'username', 'title']


class TitleAdmin(admin.ModelAdmin):
    list_display = ['profession']


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(DateAndWeek, DateAndWeekAdmin)
admin.site.register(UserAndTitle, UserAndTitleAdmin)
admin.site.register(Title, TitleAdmin)


admin.site.site_header = '打卡平台系统'
admin.site.site_title = '打卡平台系统'
