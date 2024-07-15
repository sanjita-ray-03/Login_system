from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from login_sys.models import details
# Create your views here.
def home(request):
    return render(request,"login_sys/index.html")

def signup(request):
    
    if request.method=="POST":
        username = request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        store= details(username=username, first_name=fname, last_name=lname, email=email, password=pass1)
        store.save()
        
        if User.objects.filter(username=username):
            messages.error(request,"username already exist!")
            return redirect('home')
            
            
        if User.objects.filter(email=email):
            messages.error(request,"Email already registered!")
            return redirect('home')
            
        if len(username)>20:
            messages.error(request,"Username must be under 20 characters.")
        
        if pass1 != pass2:
            messages.error(request,"Passwords didn't match")
            
        if not username.isalnum():
            messages.error(request,"Username must be alpha numeric")
            return redirect('home')
        
        
        myuser= User.objects.create_user(username,email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        
        myuser.save()
        
        messages.success(request,"Your account has been created successfully")
        return redirect('signin')
    
    
    return render(request,"login_sys/signup.html")

def signin(request):
    
    if request.method=='POST':
        username= request.POST['username']
        pass1= request.POST['pass1']
    
        user = authenticate(username= username, password= pass1) 
        
        if user is not None:
            login(request, user) 
            fname= user.first_name
            return render(request, "login_sys/index.html",{'fname': fname}) 
        
        else:
            messages.error(request,"Bad Credntials!") 
            return redirect('home')
    
    
    
    return render(request,"login_sys/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"logged out!")
    return redirect('home')