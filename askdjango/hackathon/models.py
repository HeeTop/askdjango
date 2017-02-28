from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts')
    title = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title