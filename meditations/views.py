from .models import Meditation
from django.shortcuts import render
from django.views import generic


def index(request):
    return render(request, 'meditations/index.html')    #Might need context

class MeditationListView(generic.ListView):
    model = Meditation

# class MeditationHomeView(generic.list):
#     model = Meditation