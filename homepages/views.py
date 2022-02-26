from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def indexPageView(request) :
    return render(request, 'homepages/index.html')

def primaryPageView(request) :
    return render(request, 'homepages/primarysrc.html')

def secondaryPageView(request) :
    return render(request, 'homepages/secondarysrc.html')

def testimonyPageView(request) :
    return render(request, 'homepages/testimony.html')