from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home ),
    path('contact/', views.contact ),
    path('login/', views.loginuser ),
    path('logout/', views.logoutuser ),
]

# Rough$road@4147
