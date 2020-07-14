from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.views import APIView
from django.contrib.auth.models import User
from userapp.models import UserProfile
from .serializers import UserSerializer,UserProfileSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UserProfileViewset(viewsets.ModelViewSet):
    """
    用户详细信息
    """
    queryset = UserProfile.objects.all()       # 这里只是定义了SQL语句的写法，并不会真的进行查询，只有当遍历对应数据时才会进行真正的查询
    serializer_class = UserProfileSerializer    # 序列化类
    authentication_classes = (JSONWebTokenAuthentication)