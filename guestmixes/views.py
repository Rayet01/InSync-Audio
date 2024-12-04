from django.shortcuts import render
from .models import GuestMix

def guest_mix_list(request):
    guest_mixes = GuestMix.objects.all()
    return render(request, 'guestmixes/guest_mix_list.html', {'guest_mixes': guest_mixes})
