__author__ = 'LX'

import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
User=get_user_model()
class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = User
        fields = ("username", "gender")