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
    #  we have some questions that are ask by admin these questions can have answers  or should i say comments by other users 
class Answers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)# this statement ensures that when a user gets deleted all the answers related to user gets also deleted 
    answer=models.TextField(null=True,blank=True)
    questions=models.ForeignKey(Questions, related_name="answers",on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user.username}--Answer"