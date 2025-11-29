from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from cloudinary_storage.storage import MediaCloudinaryStorage


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
    

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        storage=MediaCloudinaryStorage(),
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

    @property
    def photo_url(self):
        
        if self.photo:
            return self.photo.url
        return "https://res.cloudinary.com/dqgi7eoks/image/upload/v1764432082/default_dd0mqb.jpg"