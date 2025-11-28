from django.shortcuts import render
from .models import Event
from django.utils import timezone
# Create your views here.

def event_list(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'events.html', {'events': events})