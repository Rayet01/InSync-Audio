from django.shortcuts import render
from .models import GuestMix, Event

def index(request):
    guest_mixes = GuestMix.objects.all()[:3]  # Featured guest mixes, limit to 3
    upcoming_events = Event.objects.all()[:3]  # Upcoming events, limit to 3
    return render(request, 'home/index.html', {
        'guest_mixes': guest_mixes,
        'upcoming_events': upcoming_events,
    })
