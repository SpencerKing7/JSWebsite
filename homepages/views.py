from django.http import HttpResponse
from django.shortcuts import render

from homepages.models import Response

# Create your views here.
def indexPageView(request) :
    return render(request, 'homepages/index.html')

def primaryPageView(request) :
    return render(request, 'homepages/primarysrc.html')

def secondaryPageView(request) :
    return render(request, 'homepages/secondarysrc.html')

def testimonyPageView(request) :
    
    data = Response.objects.all().order_by('-id')

    context = {
        "data" : data
    }

    return render(request, 'homepages/testimony.html', context)

def saveTestimonyPageView(request) :
    if request.method == 'POST' :

        response = Response()

        response.name = request.POST.get('name')
        response.testimony = request.POST.get('testimony')

        try:
            response.save()

            return testimonyPageView(request)

        except:
            return HttpResponse("Error - Please try again.")

def otherSourcesPageView(request) :
    return render(request, 'homepages/othersrc.html')

    