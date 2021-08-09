from django.conf.urls import include
from django.db import router
from django.urls.conf import path
from rest_framework import routers, urlpatterns 
from .api import UserViewsets 


router = routers.SimpleRouter()
router.register('userapi',UserViewsets)

urlpatterns=[
    path('', include(router.urls))
]