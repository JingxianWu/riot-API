from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

from django.http import JsonResponse
import requests, json 

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

def summoner_name_lookup(request):
    #print(request.GET.get('summoner'))
    summoner_name = request.GET.get('summoner')
    api_key = 'RGAPI-eb7de545-9a0b-4979-97ec-41365a37c2f6'
    url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/'+summoner_name+'?api_key='+api_key
    content = requests.get(url)
    return JsonResponse(json.loads(content.content))

def ranked_lookup(request):
    summoner_id = request.GET.get('summonerId')
    api_key = 'RGAPI-eb7de545-9a0b-4979-97ec-41365a37c2f6'
    url = 'https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/'+summoner_id+'?api_key='+api_key
    content = requests.get(url)
    return JsonResponse(json.loads(content.content), safe=False)
