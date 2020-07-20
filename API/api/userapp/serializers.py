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
        fields = ("user","nickname","gender","mobile","birthday","id","icon")
        read_only_fields=['id']

        # fields=('__all__')
class UserSerializer(serializers.ModelSerializer):
    profile_of=UserProfileSerializer(required = False)
    class Meta:
        model = User
        fields = ('id','username','password','email','last_login','profile_of')
        read_only_fields=['last_login','profile_of']
        extra_kwargs={'password':{'write_only':True}}
    def create(self, validated_data):
        # validated_data['profile_of'] = null
        user=User(**validated_data)#接受前端传过来的用户名和密码
        user.set_password(validated_data['password'])#通过字典方式调用
        # validated_data['profile_of'] = self.context.get("profile_of")
        # user_profile = UserProfile.objects.create(**validated_data)
        user.save()#保存到内存中
        return user
class UserOnlySerializer(serializers.ModelSerializer):
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