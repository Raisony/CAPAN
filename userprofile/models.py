from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')

    phone = models.CharField(max_length=20, blank=True)

    email = models.CharField(max_length=20, blank=True)

    # avatar = models.ImageField(upload_to = 'avatar/%Y%m%d/', blank = True)

    resume = models.FileField(upload_to = 'resume/%Y-%m-%d/', blank = True)



    school = models.CharField(max_length=20, blank=True)

    major = models.CharField(max_length=20, blank=True)

    bio = models.TextField(max_length = 300, blank = True)

    def __str__(self):

        return 'user {}'.format(self.user.username)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:

        Profile.objects.create(user = instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()