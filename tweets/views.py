from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Tweet
# Create your views here.
def home_view(requests,*args,**kwargs):
    return HttpResponse("<h1>Hello World</h1>") # But how django will know so we add it to urls.py

def tweet_detail_view(requests, tweet_id , *args,**kwargs):
    try:
        obj = Tweet.objects.get(id = tweet_id)
    except:
        raise Http404
        return HttpResponse(f"<h1>Konichiwa {tweet_id} - {obj.content}</h1>") # But how django will know so we add it to urls.py

