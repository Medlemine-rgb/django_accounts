from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
'''je utilise One-to-One field pour concat : User + profile (les autre information de user ) 

'''
# Create your models here.

''' username  
    password 
    first_name
    laste_name
    email '''

class Profile(models.Model):
    # concatination OneToOneField
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    # les autre attribue de profile
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    addres = models.CharField(max_length=50 ,null=True,blank=True)
    img = models.ImageField(upload_to="profile_img/", default='profile_img/default.png')
    age = models.CharField(max_length=15 ,null=True,blank=True)
    created = models.DateTimeField(default=timezone.now)
    #ob
    def __str__(self) -> str:
        return str(self.user)
@receiver(post_save, sender = User)
def create_user_profile(sender,instance,created,**kwargs):
    # sender : qui envoie un signale 
    # instance de nouvelle user 
    # created : return user created or not 
    # ** kwargs : les information de user created
    if created:
        Profile.objects.create(
            user = instance
        )