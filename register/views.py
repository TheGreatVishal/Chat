from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import Friends.friends_lib as fl

# Create your views here.

def developer_info(request):
    
    return render(request,"developer_info.html")

def logout(request):
    
    auth.logout(request)
    return redirect("login")

def welcome(request):
    
    return render(request, "welcome.html")

def signup(request):
    
    if request.method == "POST":
  
        db = fl.Database()
        
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        try : 
            db.create_table_of_friends(username)     
        except : 
            pass
        
        try : 
            db.create_table_of_requests(username)     
        except : 
            pass
        
        db.close()
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username already taken!!")
                return redirect("signup")
            else: 
                user = User.objects.create_user(username = username, password = password1, first_name = first_name, last_name = last_name)
                user.save()
                # messages.info(request, "User Created Successfully!!")
                return redirect("login")
        
        else:
            messages.info(request, "Password not matching!!")
            return redirect("signup")
    else:
        return render(request,"signup.html")

def login(request):
    
    if request.method == "POST":
        
        db = fl.Database()
        
        username = request.POST["username"]
        password = request.POST["password"]
        
        try : 
            db.create_table_of_friends(username)     
        except : 
            pass
        
        try : 
            db.create_table_of_requests(username)     
        except : 
            pass
        
        db.close()
        
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request,user)
            return redirect("welcome")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")

    
    else:
        return render(request,"login.html")