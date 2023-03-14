import random
from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import render

from .form import TweetForm

from .models import Tweet
# Create your views here.
def home_view(request,*args,**kwargs):
    # return HttpResponse("<h1>Hello World</h1>") # But how django will know so we add it to urls.py
    return render(request,"pages/home.html", context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None) #TweetForm class can initialise with data(POST) or not
    if form.is_valid(): #If form is valid then do this
        obj = form.save(commit=False)
        # do other form related logic

        obj.save() #Save it to database

        form = TweetForm() #Reinitialize the form again (a blank form)
    # If not valid then do this
    return render(request,"components/form.html", context= {"form" : form})

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    return json data (why? so we can consume by javascript/java/)
    """
    qs = Tweet.objects.all() #It is grabing all the objects in tweet
    tweets_list = [{"id":x.id, "content":x.content, "likes" :random.randint(0,12345) } for x in qs] #It is a data dictionary
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id , *args,**kwargs):
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

