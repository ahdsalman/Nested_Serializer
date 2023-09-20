from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,BaseUserManager

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    place= models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    is_doctor=models.BooleanField(default=False)
    USERNAME_FIELD='username'
    


    def __str__(self) :
        return self.name
    @property
    def doctor(self):
        return self.doctor_set.all()


class Doctor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=250)
    hospital=models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.department

