from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('summoner_name_lookup/', views.summoner_name_lookup, name='name'),
    path('ranked_lookup/', views.ranked_lookup, name='ranked'),
]