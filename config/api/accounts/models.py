from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.core.validators import FileExtensionValidator

class UserManager(BaseUserManager):

    def create_user(self,first_name,last_name,username,email,password=None):

        if not username:
            raise ValueError("username is needed")
        if not email:
            raise ValueError("email is needed")
        user=self.model(
            first_name=first_name,last_name=last_name,username=username,email=self.normalize_email(email)
        )
        test=self.filter(email=email)
        if not test:
            user.set_password(password)
            user.save(using=self._db)
            return user
        else:
            raise ValueError("email allready exsist")

    def create_superuser(self,first_name,last_name,username,email,password):
        
        user=self.create_user(
            first_name=first_name,last_name=last_name,username=username,email=self.normalize_email(email),password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user





        




class User(AbstractBaseUser):

    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    username=models.CharField(max_length=200,unique=True)
    email=models.EmailField(max_length=200,unique=True)
    phone_number=models.CharField(max_length=200,null=True,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    session_token=models.CharField(max_length=200,default=0)


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username","first_name","last_name"]

    is_active.bool=True
    objects=UserManager()

    def __str__(self) -> str:
        return self.username if self.username else self.first_name

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True 
       
    

    
