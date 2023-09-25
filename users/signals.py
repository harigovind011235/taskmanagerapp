from django.contrib.auth.models import User
from .models import Employee
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def createProfile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Employee.objects.create(user=user,)
        profile.save()


