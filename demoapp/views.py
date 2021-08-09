from demoapp.models import Contact
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# home page of aplication
def home(request):
    if request.user.is_anonymous:
        return  redirect('/demoapp/login/') 
          
    return render(request , 'home.html')


# register user 
def contact(request):
    if request.method == 'POST':
        Username=request.POST.get('Username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user= User(username=Username ,email=email ,password=password )
        user.save()
    return render(request , 'contact.html')

# login user 
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/demoapp/home/')
        else:
            return render(request, 'contact.html')

    return render(request, 'loginuser.html')


# logout user     
def logoutuser(request):
    logout(request)
    return render(request , 'loginuser.html')
