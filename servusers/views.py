from rest_framework import generics
from .models import Servusers
from .serializers import ServusersSerializer

class ServusersAPIView(generics.ListAPIView): #Представление 
    queryset = Servusers.objects.all()
    serializer_class = ServusersSerializer
    