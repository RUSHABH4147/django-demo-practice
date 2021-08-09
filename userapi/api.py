from rest_framework import viewsets,permissions
from .serializers import UserSerializers
from .models import Apiuser

class UserViewsets(viewsets.ModelViewSet):
    queryset = Apiuser.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=UserSerializers