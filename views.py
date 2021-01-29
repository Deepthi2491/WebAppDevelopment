from django.shortcuts import render
from .models import Destination
from django.http import HttpResponse
# Create your views here.
#def Home(request):
#    return render(request,'DEMOAPP/Home.html')
def Home(request):
    dests = Destination.objects.all()
    return render(request, 'DEMOAPP/Home.html', {'dests': dests})
def Link(request):
    return render(request,'DEMOAPP/Click.html')
def Edu(request):
    return render(request,'DEMOAPP/Edu.html')
