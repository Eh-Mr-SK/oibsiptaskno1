from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TODO(models.Model):
    status_choices = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
    ]

    title = models.CharField(max_length=50)
    created = timezone.now()
    status = models.CharField(max_length=2 , choices=status_choices)
    user  = models.ForeignKey(User  , on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank = True)
    