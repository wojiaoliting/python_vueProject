__author__ = 'LX'

import re
from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime
from userapp.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    class Meta:
        model = UserProfile
        fields = ("user","nickname", "gender")
        # fields=('__all__')
class UserSerializer(serializers.ModelSerializer):
    profile_of=UserProfileSerializer()
    class Meta:
        model = User
        fields = ('id','username','email','last_login','profile_of')
        order = ('-id')

