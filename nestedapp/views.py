from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class userView(APIView):
    def get(self,request):
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
        


class DoctorView(APIView):
    def get(self,request):
        doctor=Doctor.objects.all()
        serializer=DoctorSerializer(doctor,many=True)
        return Response(serializer.data)
        
    

class userOnlyView(APIView):
    def get(self,request):
        user=User.objects.filter(is_doctor=False)
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
    
class DoctorOnlyView(APIView):
    def get(self,request):
        doctor=User.objects.filter(is_doctor=True)
        serializer=UserSerializer(doctor,many=True)
        return Response(serializer.data)
        