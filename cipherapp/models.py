from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_text = models.TextField()
    encrypted_text = models.TextField()
    method = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)