__author__ = 'LX'

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    # 利用内部Meta类来进行元数据配置项的设置
    class Meta:
        verbose_name = "用户"     # 对象名（单数）
        verbose_name_plural = verbose_name  # 对象名（复数）

    def __str__(self):
        return self.username

from django.contrib.auth import get_user_model
User = get_user_model()