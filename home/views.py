from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/loginUser")
    return render(request,'index.html')
def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)

        #check if user has correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
        # A backend authenticated the credentials
            return redirect("/")
        else:
        # No backend authenticated the credentials

            return render(request,'loginUser.html')
    return render(request,'loginUser.html')
def logoutUser(request):
    logout(request)
    return redirect("/loginUser")
