from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Questions(models.Model):
    title=models.CharField(max_length=10000)
    description=models.TextField(null=True,blank=True)
    dateCreated=models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username}--questions"
    