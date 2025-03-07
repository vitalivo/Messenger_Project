from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.username

class Room(models.Model):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='rooms')

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


