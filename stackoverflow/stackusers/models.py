from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to='Profile_pic/',
        default='default.jpg',
        null=True,
        blank=True
    )
    bio=models.CharField(max_length=1000,null=True,blank=True)
    phone=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
