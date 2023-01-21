from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Servusers
from .serializers import ServuserSerializer




class ServusersAPIView(APIView): #Представление 
    
    def get(self,request):
        s = Servusers.objects.all()
        return Response({'posts': ServuserSerializer(s, many = True).data})


    
    