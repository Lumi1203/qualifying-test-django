from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    SELECT_ROLE = (
        ("testtaker", "Test Taker"),("examiner", "Examiner"),
    )

    role = models.CharField(max_length=20, choices= SELECT_ROLE, default= "testtaker")
    examiner_id = models.CharField(max_length= 10, blank= True, null= True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', default='default.jpg')

    def __str__(self):
        return f"{self.user.username}'s Profile"
