import email
import imp
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned


class EmailBackend(ModelBackend):
    ''''check username and password is a valid user ''' 
    def authenticate(self, request, username=None , password =None, **kwargs):
        try : 
            #chercher par username ou email pas de password 
            user = User.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username)
            )
        except User.DoesNotExist:
            print("Ops... user DoesNotExist")
        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        
    ''''check username and password is a valid user ''' 
    def  get_user(self, user_id):
        try :
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None