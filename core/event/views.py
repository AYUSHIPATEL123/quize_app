from django.shortcuts import render
from .models import Event
from django.utils import timezone
from django.contrib.auth.decorators import login_required 
# Create your views here.
@login_required(login_url='login')
def event_list(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'events.html', {'events': events})
