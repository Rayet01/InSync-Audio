from django.shortcuts import render
from .models import GuestMix, Event  

def index(request):
    # Select a specific mix to feature, e.g., the latest mix
    featured_mix = GuestMix.objects.filter(is_featured=True).first()

    return render(request, 'home/index.html', {'featured_mix': featured_mix})

