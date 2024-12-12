from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated 
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from .permissions import IsAuthenticatedAdministration

class SubjectListApi(APIView):
    def get(self, request):
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data)

class SubjectAddApi(APIView):
    permission_classes=[IsAuthenticatedAdministration]
    def post(self, request):
        serializer= SubjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class SubjectDetailGetApi(APIView):
    def get(self, request, pk):
        subject= get_object_or_404(Subject, pk=pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

class SubjectDetailUpdateApi(APIView):
    permission_classes=[IsAuthenticatedAdministration]
    def put(self, request, pk):
        subject= get_object_or_404(Subject, pk=pk)
        serializer = SubjectSerializer(subject, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectDetailDeleteApi(APIView):
    permission_classes=[IsAuthenticatedAdministration]
    def delete(self, request, pk):
        subject= get_object_or_404(Subject, pk=pk)
        subject.is_deleted = True
        subject.save()
        return Response(status = status.HTTP_204_NO_CONTENT)