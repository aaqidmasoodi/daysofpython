from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()


    def __str__(self):
        return self.user.username
    
    

class Catagory(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title



class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    comment_count = models.IntegerField(default=0)
    thumbnail = models.ImageField()
    date_posted = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    catagories = models.ManyToManyField(Catagory)

    def __str__(self):
        return self.title
