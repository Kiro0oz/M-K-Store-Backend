from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    rest_password_token = models.CharField(max_length=50, default='', blank=True)
    rest_password_token_expiry = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    


@receiver(post_save, sender=User)
def save_profile(sender,instance, created, **kwargs):

    print('instance',instance)
    user = instance

    if created:
        profile = Profile(user = user)
        profile.save()
     