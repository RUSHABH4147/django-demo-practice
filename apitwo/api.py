from rest_framework import viewsets,permissions
from .serializer import ApiSerilizer
from .models import Apiuser

class apitwoViewet(viewsets.ModelViewSet):
    queryset = Apiuser.objects.all()

    permission_classes =[
        permissions.AllowAny
    ]
    serializer_class=ApiSerilizer