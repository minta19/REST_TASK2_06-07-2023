from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Student

class StudentViewcreate(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def post(self, request, *args, **kwargs):
        response= super().post(request, *args, **kwargs)
        return Response({'message':'Student added'})
    
class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def delete(self, request, *args, **kwargs):
        response= super().delete(request, *args, **kwargs)
        return Response({'Message':'Student Deleted !!'})