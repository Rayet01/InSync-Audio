from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_mix_list, name='guest_mix_list'),
]
