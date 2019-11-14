from django.db import models


class UserInfo(models.Model):
    """
    用户表
    """
    uid = models.IntegerField(auto_created=True, primary_key=True, verbose_name="用户ID")
    job = models.CharField(max_length=10, db_index=True, unique=True, verbose_name="用户工号")
    username = models.CharField(max_length=10, verbose_name="用户名")
    image = models.CharField(max_length=10, verbose_name="图片地址")
    password = models.CharField(max_length=64, verbose_name="密码")
    email = models.CharField(max_length=20, verbose_name="邮箱")


class Title(models.Model):
    """
    称谓
    """
    profession = models.CharField(max_length=10, verbose_name="称号")


class UserAndTitle(models.Model):
    """
    关联表
    """
    id = models.IntegerField(auto_created=True, primary_key=True, db_index=True)
    username = models.ForeignKey(to=UserInfo, to_field="job", on_delete=models.SET_NULL, verbose_name="用户")
    title = models.ForeignKey(to=Title, to_field="profession", on_delete=models.SET_NULL, verbose_name="职称")


class DateAndWeek(models.Model):
    """
    时间记录表
    """
    user = models.ForeignKey(to=UserInfo, to_field="job")
    time = models.DateTimeField(verbose_name="签到时间", default="")
    status = models.CharField(max_length=20, verbose_name="状态", default="未签到")