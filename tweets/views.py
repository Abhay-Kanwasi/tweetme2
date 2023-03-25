import random
from django.conf import settings
from django.http import HttpResponse,Http404,JsonResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
# from django.utils.http import is_safe_url
from .form import TweetForm
from .models import Tweet
from .serializers import TweetSerializer, TweetActionSerializer

from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated


# ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request,*args,**kwargs):
    """
    REST API Create View -> DRF(Django Rest Framwork)
    """
    # return HttpResponse("<h1>Hello World</h1>") # But how django will know so we add it to urls.py
    return render(request,"pages/home.html", context={}, status=200)

@api_view(['POST'])
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated]) #If they are authenticated only then they can access
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data = request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({},status = 400)


@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id = tweet_id) #qs = query set
    if not qs.exists():
        return Response({},status=404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status = 200)

# Checking permission that this particular user can delete tweet and it's on the server side
@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id = tweet_id) #qs = query set
    if not qs.exists():
        return Response({},status=404)
    qs = qs.filter(user= request.user)
    if not qs.exists():
        return Response({"message":"You cannot delete this tweet"}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message":"Tweet removed"}, status = 200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
    '''
    id is required
    Action options are: like, unlike, retweet
    '''
    serializer = TweetSerializer(data = request.POST)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get("id")
        action = data.get("action")
        qs = Tweet.objects.filter(id = tweet_id) #qs = query set
        if not qs.exists():
            return Response({},status=404)
        obj.likes.add(request.user)
        obj = qs.first()
        if action == "like":
            obj.likes.add(request.user)
        elif action == "unlike":
            obj.likes.remove(request.user)
        elif action == "retweet":
            # this is todo
            pass
        else:
            obj.likes.add(request.user) 
    return Response({"message":"Tweet removed"}, status = 200)

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all() #qs = query set
    serializer = TweetSerializer(qs, many = True)
    return Response(serializer.data)










def tweet_create_view_pure_django(request, *args, **kwargs):
    user = request.user
    if not request.user.is_authenticated:
        user = None
        # if request.is_ajax():
        #     return JsonResponse({}, status = 401)
        # return redirect(settings.LOGIN_URL)
    form = TweetForm(request.POST or None) #TweetForm class can initialise with data(POST) or not
    next_url = request.POST.get("next") or None
    if form.is_valid(): #If form is valid then do this
        obj = form.save(commit=False)
        # do other form related logic
        obj.user = request.user or None
        obj.save() #Save it to database
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201) #201 = created items
        if next_url != None :
            return redirect(next_url)

        form = TweetForm() #Reinitialize the form again (a blank form)
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors,status = 400)
    # If not valid then do this
    return render(request,"components/form.html", context= {"form" : form})

def tweet_list_view_pure_django(request, *args, **kwargs):
    """
    REST API VIEW
    return json data (why? so we can consume by javascript/java/)
    """
    qs = Tweet.objects.all() #It is grabing all the objects in tweet
    tweets_list = [x.serialize() for x in qs] #It is a data dictionary
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view_pure_django(request, tweet_id , *args,**kwargs):
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

