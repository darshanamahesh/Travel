from django.shortcuts import render
from django.http import HttpResponse
from . models import Place,Teams
# Create your views here.

def demo(request):
    obj=Place.objects.all()
    team1=Teams.objects.all()
    return render(request,"index.html", {'obj1':obj,'team1':team1})



