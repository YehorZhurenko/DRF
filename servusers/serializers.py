from rest_framework import serializers
from .models import Servusers

""" class ServusersSerializer(serializers.ModelSerializer): #Сам сериализатор
    class Meta:
        model = Servusers
        fields = ('name', 'sname') 

class Servuser:
    def __init__(self, name, sname):
        self.name = name
        self.sname = sname
 """
class ServuserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 30)
    sname = serializers.CharField(max_length = 30)
    email = serializers.EmailField(max_length = 30)
    spec = serializers.CharField(max_length = 30)

    def create(self, validated_data):
        return Servusers.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get("name", instance.name)
        instance.sname = validate_data.get("sname", instance.sname)
        instance.email = validate_data.get("email", instance.email)
        instance.spec = validate_data.get("spec", instance.spec)        
        instance.save()
        return instance