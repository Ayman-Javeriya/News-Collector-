from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    news_api_request = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=64fbab8b5b994c4a88fdf343f06dd682')
    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api' : api})
    
