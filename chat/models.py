from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    name = models.CharField(max_length=50)
    member = models.ManyToManyField(User, related_name='conversations')


class Message(models.Model):
    text = models.TextField(max_length=1000)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
