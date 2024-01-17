from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):
    # dests = Destination.objects.all()
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    #dest1.img = 'img/place/1.png'
    dest1.price = 700
    # dest1.offer = False
    dests = [dest1] # used to make one 
    # return render(request,"index.html")  # this will not change the values 
    #return render(request, "index.html", {'dest1': dest1})   # this will change the values 
    return render(request, "index.html", {'dests': dests}) # this make all the things in one 