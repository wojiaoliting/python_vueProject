__author__ = 'LX'


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
    # profile_of=UserProfileSerializer()
    class Meta:
        model = User
        fields = ('id','username','password','email','last_login')
        read_only_fields=['last_login']
        extra_kwargs={'password':{'write_only':True}}
    def create(self, validated_data):
        user=User(**validated_data)#接受前端传过来的用户名和密码
        user.set_password(validated_data['password'])#通过字典方式调用
        user.save()#保存到内存中
        return user