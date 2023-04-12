from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length = 200, null = True, blank = True)
    location = models.CharField(max_length = 200, null = True, blank = True)
    short_intro = models.CharField(max_length = 500, null = True, blank = True)
    bio = models.TextField(null = True, blank = True)
    profile_image = models.ImageField(null = True, blank = True, 
                                      default="https://res.cloudinary.com/dnoomtyyx/image/upload/v1681232648/static/images/profiles/user-default.bf40b0e86c9d.png",
                                      upload_to="profiles/")
    github_link = models.CharField(max_length = 500, null = True, blank = True)
    linkedin_link = models.CharField(max_length = 500, null = True, blank = True)
    website_link = models.CharField(max_length = 500, null = True, blank = True)
    twitter_link = models.CharField(max_length = 500,null = True, blank = True)
    created = models.DateTimeField(auto_now_add  = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, editable = False, primary_key = True)

    def __str__(self):
        return str(self.username)
    
    class Meta:
        ordering = ['created']


class skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True, blank =  True)
    name = models.CharField(max_length=200, null = True, blank=True)
    description = models.TextField(max_length = 300, null= True, blank = True)
    created = models.DateTimeField(auto_now_add  = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, editable = False, primary_key = True)

    def __str__(self):
        return str(self.name) # type: ignore
    

