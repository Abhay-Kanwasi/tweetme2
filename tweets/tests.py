from django.contrib.auth import get_user_model # Because we need the user info here
from django.test import TestCase
from .models import Tweet

# This module framework is taken from rest api testing section
from rest_framework.test import APIClient


# Create your tests here.(Run through entire twitter api by just running these tests)
User = get_user_model()

class TweetTestCase(TestCase):
    # Here setUp is a build in method which help us to create all the instances
    def setUp(self): # setUp is the only place to update test database
        self.user = User.objects.create_user(username = "abc", password = "somepassword")
        self.userb = User.objects.create_user(username = "abc-2", password = "somepassword2")
        Tweet.objects.create(content="my first tweet", user = self.user)
        Tweet.objects.create(content="my second tweet", user = self.user)
        Tweet.objects.create(content="my third tweet", user = self.userb)
        self.currentCount = Tweet.objects.all().count()
    
    
    def test_tweet_created(self):
        tweet_obj = Tweet.objects.create(content="my forth tweet", user = self.user)
        self.assertEqual(tweet_obj.id, 4)
        self.assertEqual(tweet_obj.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username = self.user.username, password = 'somepassword')
        return client

    def test_tweet_list(self):
        client = self.get_client() # login
        response = client.get("/api/tweets/") # grab those tweets
        self.assertEqual(response.status_code, 200) # and return 200
        self.assertEqual(len(response.json()), 1)

    def test_tweet_list(self):
        client = self.get_client() # login
        response = client.get("/api/tweets/") # grab those tweets
        self.assertEqual(response.status_code, 200) # and return 200
        self.assertEqual(len(response.json()), 3)

    def test_action_like(self):
        client = self.get_client() # login
        response = client.post("/api/tweets/action/", {"id": 1, "action": "like"}) # hit like
        self.assertEqual(response.status_code, 200) # and return 200
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 1) # like count is 1

    def test_action_unlike(self):
        client = self.get_client() # login
        response = client.post("/api/tweets/action/", {"id": 2, "action": "like"}) # hit like
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/tweets/action/", {"id": 2, "action": "unlike"}) # hit unlike
        self.assertEqual(response.status_code, 200) # and return 200
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 0) # like count is 0
        
    def test_action_retweet(self):
        client = self.get_client() # login
        response = client.post("/api/tweets/action/", {"id": 2, "action": "retweet"}) # hit like
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_tweet_id = data.get("id")
        self.assertNotEqual(2, new_tweet_id)
        self.assertEqual(self.currentCount + 1, new_tweet_id)

    
    def test_tweet_create_api_view(self):
        request_data = {"content" : "This is my tweet"}
        client = self.get_client()
        response = client.post("/api/tweets/create/", request_data) # hit like
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        new_tweet_id = response_data.get("id")
        self.assertEqual(self.currentCount + 1, new_tweet_id)

    def test_tweet_detail_api_view(self):
        client = self.get_client()
        response = client.get("/api/tweets/1/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        _id = data.get("id")
        self.assertEqual(_id, 1)

    def test_tweet_delete_api_view(self):
        client = self.get_client()
        response = client.delete("/api/tweets/1/delete/")
        self.assertEqual(response.status_code, 200)
        response = client.delete("/api/tweets/1/delete/")
        self.assertEqual(response.status_code, 404)

        response_incorrect_owner = client.delete("/api/tweets/3/delete/")
        self.assertEqual(response_incorrect_owner.status_code, 401)
        