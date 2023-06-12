from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('med_list/', views.MeditationListView.as_view(), name='med_list'),
]