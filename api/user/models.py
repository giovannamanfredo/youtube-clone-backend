from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

class Creator(AbstractUser):

    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), blank=False)

    channel_name = models.CharField(max_length=50, blank=True)
    is_channel_active = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    profile_link = models.CharField(_("profile link"), max_length=255, blank=True)
    cover_link = models.CharField(_("cover link"), max_length=255, blank=True)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
