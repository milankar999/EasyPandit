from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null = True, blank = True)
    mobile = models.CharField(max_length = 15)
    
    def __str__(self):
        return  self.user.username+ ' / ' + self.user.first_name + ' ' + self.user.last_name


@receiver(post_save,sender=User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()