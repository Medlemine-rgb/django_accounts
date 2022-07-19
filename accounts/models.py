from django.db import models
from django.contrib.auth.models import User


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
    #imge 
    # age 
    #ob
    def __str__(self) -> str:
        return str(self.user)