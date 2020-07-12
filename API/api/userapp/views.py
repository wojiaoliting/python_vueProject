from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from .serializers import UserDetailSerializer
from rest_framework.views import APIView
# Create your views here.
User = get_user_model()
class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer    # 序列化类
    queryset = User.objects.all()       # 这里只是定义了SQL语句的写法，并不会真的进行查询，只有当遍历对应数据时才会进行真正的查询
    authentication_classes = (JSONWebTokenAuthentication, )