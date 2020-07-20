"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from api.settings import MEDIA_ROOT
from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from userapp.views import UserViewSet,UserProfileViewset

router = DefaultRouter()
router.register(r'admins', UserViewSet)
router.register(r'profile', UserProfileViewset)
urlpatterns = [
    url(r'^', include(router.urls)), 
    url(r'docs/', include_docs_urls(title="APP Inventor案例库")),      # 自动生成的API说明文档
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^login/', obtain_jwt_token),
    url(r'^api/token/obtain/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),	# 需要添加的内容
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),	# 需要添加的内容

]

urlpatterns.extend([
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),     # path 将作为第二参数传到server进行处理
])
