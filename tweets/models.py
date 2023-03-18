import random
from django.db import models

#user creation 
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class Tweet(models.Model):
    # We can have three types of data as tweets : id text image
    #It also created a column name id by default in our database
    #id = models.AutoField(primary_key=True) 

    user = models.ForeignKey(User, on_delete=models.CASCADE)
     #ForeignKey : user can do many tweets but one tweet belong to it's own user.
     #CASCADE :If user is deleted then all the tweets by user will also be deleted.

    #It will create a column name content in our database
    content = models.TextField(blank=True, null=True)

    # It will create a image column in our database
    image = models.FileField(upload_to="images/", blank=True, null=True) #blank = not required in django | null = not required in database

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return{
            "id":self.id,
            "content":self.content,
            "likes":random.randint(0,200)
        }
