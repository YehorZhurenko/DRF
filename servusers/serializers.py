from rest_framework import serializers
from .models import Servusers

class ServusersSerializer(serializers.ModelSerializer): #Сам сериализатор
    class Meta:
        model = Servusers
        fields = ('name', 'sname') 

class Servuser:
    def __init__(self, name, sname):
        self.name = name
        self.sname = sname

class ServuserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)

