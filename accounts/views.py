from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

user_created=0

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request,'invalid credentials!')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        if(request.POST['email']==''):
            messages.info(request,'Email Required')
            return redirect('register')

        if(request.POST['username']==''):
            messages.info(request,'Username Required')
            return redirect('register')

        if(request.POST['Password1']==''):
            messages.info(request,'Password Required')
            return redirect('register')

        if(request.POST['Password2']==''):
            messages.info(request,'Passwords does not match!')
            return redirect('register')         

          

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                messages.success(request,'Account Created Successfully!')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/') 

