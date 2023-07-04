from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class CustomUserManager(BaseUserManager):
     def create_user(self, customer_xid, **extra_fields):
        if not customer_xid:
            raise ValueError('The customer_xid field must be set')
        user = self.model(customer_xid=customer_xid, **extra_fields)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
     customer_xid = models.UUIDField(
         editable = False,
         unique=True,
         blank=False
    )
     id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False
         )
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     # overwrite the username field
     USERNAME_FIELD = 'customer_xid'

     objects = CustomUserManager()

         
     def __str__(self):
        return str(self.id)

