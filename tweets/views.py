from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from .models import Tweet
# Create your views here.
def home_view(requests,*args,**kwargs):
    return HttpResponse("<h1>Hello World</h1>") # But how django will know so we add it to urls.py

def tweet_detail_view(requests, tweet_id , *args,**kwargs):
    """
    REST API VIEW
    return json data (why? so we can consume by javascript/java/)
    """
    data = {
        "id" : tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id = tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404
    
    return JsonResponse(data,status=status) # But how django will know so we add it to urls.py

