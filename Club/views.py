from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Event, Meeting, Minutes, Resource

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def getresources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html' , {'resource_list' : resource_list})

def getmeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html' , {'meeting_list' : meeting_list})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={
        'meet' : meet,
    }
    return render(request, 'Club/meetingdetails.html', context=context)