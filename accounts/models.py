from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='profiles', blank=True, null=True, default='anonimus.jpg')

    def __str__(self):
        return self.user.username