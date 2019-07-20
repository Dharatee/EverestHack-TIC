from django.shortcuts import render

# Create your views here.
def request(request):
    return render(request,'request.html')