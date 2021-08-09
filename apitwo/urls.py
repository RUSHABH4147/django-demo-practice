from rest_framework import routers, urlpatterns
from .api import apitwoViewet

router = routers.DefaultRouter()

router.register('apitwo',apitwoViewet)

urlpatterns=router.urls