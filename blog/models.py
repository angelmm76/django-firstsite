from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    blogpost_title = models.CharField(max_length=200)
    blogpost_content = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images')  # /%Y/%m/%d')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    # author = models.ForeignKey('UserProfile')

    def __unicode__(self):
        return self.blogpost_title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    votes = models.IntegerField(default=0)
    occupation = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)

class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost)
    # user = models.OneToOneField(User)
    user = models.ForeignKey(User)
    comment_content = models.TextField(max_length=2000)
    created = models.DateTimeField('created')
