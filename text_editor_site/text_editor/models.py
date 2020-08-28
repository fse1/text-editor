from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  content = models.TextField()
  creation_time = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)