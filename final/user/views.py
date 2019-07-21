from django.shortcuts import render,redirect
from hospital.models import doctorData
from . models import requestData
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
import smtplib

# Create your views here.

docnames = doctorData.objects.values_list('First_Name')

docnames = [d[0] for d in docnames]




   
def request(request):
    if request.method=="POST":
        f_name = request.POST['first_name'] 
        m_name = request.POST['middle_name']
        l_name = request.POST['last_name']
        email = request.POST['email']    
        doctor =request.POST['doctor'] 
       
        
        user= requestData(First_Name=f_name,Middle_Name=m_name,Last_Name=l_name,Email=email,Doctor_Name=doctor)
        user.save()
        
        
        
        return render (request,'resultrequest.html')

        
        


    else:
        return render(request,'request.html',{'docname':docnames})


def prediction(request):
    return render(request,'prediction.html')
        
    
       