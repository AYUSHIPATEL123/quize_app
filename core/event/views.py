from django.shortcuts import render
from .models import Event
from django.utils import timezone
from django.contrib.auth.decorators import login_required 
# Create your views here.
@login_required(login_url='login') # Ensure user is logged in to access this view
def event_list(request):   # View to list upcoming events
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    Event.objects.filter(date__lt=timezone.now()).delete()  # Delete past events
    return render(request, 'events.html', {'events': events})
