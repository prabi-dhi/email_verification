from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAdministrationOrTeacherSelf
from .permissions import IsAdministration
from django.shortcuts import get_object_or_404

class TeacherListApi(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer= TeacherSerializer(teacher, many= True)
        return Response(serializer.data)

class TeacherDetailGetApi(APIView):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk = pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
class TeacherDetailUpdateApi(APIView):
    permission_classes=[IsAdministrationOrTeacherSelf]
    def patch(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def get_object(self):
        return Teacher.objects.get(pk=self.kwargs['pk'])

class TeacherDetailDeleteApi(APIView):
    permission_classes = [IsAdministration]
    def delete(self, request, pk):
        teacher= get_object_or_404(Teacher, pk=pk)
        teacher.is_deleted = True
        teacher.save()
        return Response(status = status.HTTP_204_NO_CONTENT)
    