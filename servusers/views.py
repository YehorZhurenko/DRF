from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Servusers
from .serializers import ServuserSerializer




class ServusersAPIView(APIView): #Представление 
    
    def get(self,request):
        s = Servusers.objects.all()
        return Response({'posts': ServuserSerializer(s, many = True).data})


    def post(self, request):
        serializer = ServuserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Servusers.objects.get(pk = pk)
        except:
            return Response({"error":"Object does not exist"})

        serializer = ServuserSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        instance = Servusers.objects.get(pk = pk)
        instance.delete()

        return Response({"post": "delete post" + str(pk)})