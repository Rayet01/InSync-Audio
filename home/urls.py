from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Root path for home page
]
