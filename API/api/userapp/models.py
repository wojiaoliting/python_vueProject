__author__ = 'LX'

from datetime import datetime
from django.db import models
from django.conf import settings
# Create your models here.
class UserProfile(models.Model):
    """
    用户档案
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_of',)
    nickname = models.CharField(max_length=30, null=True, blank=True, verbose_name="昵称")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    icon = models.ImageField(blank=True, null=True, max_length=200, upload_to='media/uploads/%Y/%m/%d/')
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=13, verbose_name="电话")
    created = models.DateTimeField('发布时间',auto_now_add=True)
    updated = models.DateTimeField('修改时间',auto_now=True)
    
    # 利用内部Meta类来进行元数据配置项的设置
    class Meta:
        verbose_name = "用户"     # 对象名（单数）
        verbose_name_plural = verbose_name  # 对象名（复数）

    def __str__(self):
        return self.user
