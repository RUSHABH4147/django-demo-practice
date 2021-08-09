from rest_framework import serializers
from .models import Apiuser


class ApiSerilizer(serializers.ModelSerializer):
    class Meta:
        model =Apiuser
        fields = "__all__"