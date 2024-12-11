from classroom.models import Classroom
from classroom.serializers import ClassroomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedAdministration
from django.shortcuts import get_object_or_404

class ClassroomListGetApi(APIView):
    def get(self, request):
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many= True)
        return Response(serializer.data)

class ClassroomAddApi(APIView):
    permission_classes=[IsAuthenticatedAdministration]
    def post(self, request):
        serializer = ClassroomSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassroomDetailGetApi(APIView):
    def get(self, request, pk):
        classroom = get_object_or_404(Classroom, pk=pk)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)

class ClassroomDetailUpdateApi(APIView):
    permission_classes=[IsAuthenticatedAdministration]
    def put(self, request, pk):
        classroom = get_object_or_404(Classroom, pk=pk)
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassroomDetailDeleteApi(APIView):
    permission_classes= [IsAuthenticatedAdministration]
    def delete(self, request, pk):
        classroom = get_object_or_404(Classroom, pk = pk)
        classroom.is_deleted = True
        classroom.save()
        return Response(status = status.HTTP_204_NO_CONTENT)