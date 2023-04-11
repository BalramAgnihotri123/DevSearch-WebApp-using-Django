from django.db import models
import uuid
from users.models import Profile
# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile, null = True, blank = True, on_delete=models.SET_NULL)
    Title = models.CharField(max_length = 200)
    Description = models.TextField(max_length = 2000, null = True, blank = True)
    demo_link = models.CharField(max_length = 2000, null = True, blank = True)
    source_link = models.CharField(max_length = 2000, null = True, blank = True)
    featured_images = models.ImageField(blank=True, null=True, default='default.jpg')
    tags = models.ManyToManyField("Tag")
    vote_ratio = models.IntegerField(default = 0, null = True, blank = True)
    vote_count = models.IntegerField(default = 0, blank = True, null = True)
    created = models.DateTimeField(auto_now_add  = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, editable = False,primary_key = True)

    def __str__(self):
       return self.Title
    
    class Meta:
        ordering = ['-created']

    @property
    def VoteCalc(self):
        reviews = self.review_set.all() #type: ignore
        positive_votes = reviews.filter(vote = "up").count()
        total_votes = reviews.count()
        ratio = (positive_votes/total_votes)*100
        self.vote_ratio = ratio
        self.vote_count = total_votes
        self.save()

    @property
    def reviewers(self):
        reviewers = self.review_set.all().values_list("owner", flat = True) #type: ignore
        return reviewers

class Review(models.Model):
    Vote_Type = (
        ('up', 'upVote'),
        ('down', 'downVote')
    )
    owner = models.ForeignKey(Profile, null=True, on_delete = models.CASCADE)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    body = models.TextField(max_length = 2000, null = True, blank = True)
    vote = models.CharField(max_length = 200, choices = Vote_Type)
    created = models.DateTimeField(auto_now_add  = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, editable = False,primary_key = True)

    def __str__(self):
        return self.body
    
    class Meta:
        unique_together = ['owner', 'project']
    

class Tag(models.Model):
    tag_name = models.TextField(max_length = 200)
    created = models.DateTimeField(auto_now_add  = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, editable = False,primary_key = True)

    def __str__(self):
        return self.tag_name