from django.shortcuts import render
from . models import doctorData
from django.http import HttpResponse

# Create your views here.
def enterdata(request):
    if request.method == "POST":
        f_name = request.POST['first_name']
        m_name = request.POST['middle_name']
        l_name = request.POST['last_name']
        address = request.POST['address']
        email = request.POST['email']
        time = request.POST['from'] +"-"+ request.POST['to']
        
        user = doctorData(First_Name=f_name,Middle_Name=m_name,Last_Name=l_name,Address=address,Email=email,Availabilty=bool(1),Time=time)
        user.save()
        return HttpResponse("<h1>success<h1>")
    else:
        return render(request,'enterdata.html')