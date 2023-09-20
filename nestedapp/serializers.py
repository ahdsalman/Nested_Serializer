from rest_framework import serializers
from .models import *



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=['department','hospital']



class UserSerializer(serializers.ModelSerializer):
    doctor=DoctorSerializer(many=True) 
    class Meta :
        model=User
        fields=['id','email','name','username','place','doctor','is_doctor']




