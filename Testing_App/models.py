from django.db import models
from  django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_photo = models.ImageField(upload_to="images")
    bio = models.CharField(max_length=750)

class Posts  (models.Model):
    text = models.CharField(max_length=750)
    added_at = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Comments  (models.Model):
    text = models.CharField(max_length=750)
    added_at = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)