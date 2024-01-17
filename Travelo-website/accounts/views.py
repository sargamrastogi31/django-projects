from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# def login(request):
#     if request.method== 'POST':
#         user_name = request.POST['user_name']
#         password = request.POST['password']
#         User = auth.authenticate(user_name=user_name, password=password)
#         if User is not None:
#             auth.login(request,User)
#             return redirect('/')
#         else:
#             messages.info(request,'invalid credentials')
#             return redirect('login')
#     else:
#         return render(request, 'register.html')

# Create your views here.
def register(request):
    if request.method == 'Post':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
           if User.objects.filter(user_name=user_name).exists():
            #    messages.info(request,'username taken') # this for screen of user 
              print('username taken') # this is used to print on console
           elif User.objects.filter(email=email).exists():
                # messages.info(request,'email taken')
               print('email taken')
           else:
               User.objects.create_user(user_name= user_name, password=password1, email=email,first_name=first_name,last_name=last_name)
               User.save()
            #    messages.info(request,'username created')
            #    return redirect('login')
               print('user create')
        else:
            #  messages.info(request,'password not matching')
            print('password not maching')
            #  return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
#get request is used to get the data
# post request is used to submit the data 
# def logout(request):
#     auth.logout(request)
#     return redirect('/')