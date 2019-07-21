from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import registration

# Create your views here.
def register(request):
    if request.method == "POST":
        f_name = request.POST['first_name']
        m_name = request.POST['middle_name']
        l_name = request.POST['last_name']
        u_name = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        bloodgroup = request.POST['blood_group']
        
         
        if (pass1!=pass2):
            messages.info(request,'PASSWORD MISMATCHED!!')
            return redirect('register')
        elif(User.objects.filter(username=u_name).exists()):
            messages.info(request,'Username already taken!!')
            return redirect('register')
        elif(User.objects.filter(email=email).exists()):
            messages.info(request,'Email already Used!!')
            return redirect('register')
        else:
            user1 = registration(First_Name=f_name,Middle_Name=m_name,Last_Name=l_name,Username=u_name,Password=pass1,Email=email,Contact=contact,Address=address,Blood_Group=bloodgroup)
            user = User.objects.create_user(username=u_name,first_name=f_name,last_name=l_name,password=pass2,email=email)
            user1.save()
            user.save()
            return redirect('/account/login')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == "POST":
        u_name = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=u_name,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials!!!!")
            return redirect('login')
    else:
        return render (request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
   