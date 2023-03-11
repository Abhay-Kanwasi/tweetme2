from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(requests,*args,**kwargs):
    return HttpResponse("<h1>Hello World</h1>") # But how django will know so we add it to urls.py

def tweet_detail_view(requests, tweet_id , *args,**kwargs):
    return HttpResponse(f"<h1>Hello {tweet_id}</h1>") # But how django will know so we add it to urls.py

