from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def authlogin(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(request,username=name,password=password)

        if user is not None:
            login(request,user)
            return redirect('employee.profile')
        else:
            messages.error(request, 'Your email or password is invalid!!')

    return render(request,'authentication/login.html')

def authregistration(request):

    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        
        if password==confirm_password:
           if User.objects.filter(username=username).exists():
               messages.error(request, 'Your username already exists!!')
           elif User.objects.filter(email=email).exists(): 
               messages.error(request, 'Your email already exists!!')  
           else:
               user=User.objects.create_user(username=username,password=password,email=email)
               user.save();
               return redirect('employee.profile')    

        else:
           messages.error(request, 'Your password or confirm_password not matched!!!!') 
    
    return render(request,'authentication/registration.html')

def forgotpassword(request):
    return render(request,'authentication/forgot.html')
    
def userlogout(request):

    logout(request)
    messages.success(request, 'Successfully logout!!!')
    return redirect('login')
