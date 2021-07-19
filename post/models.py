from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.conf.urls.static import static

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
               
    
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True)
    category = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)
        
    def __str__(self):
        return self.title




