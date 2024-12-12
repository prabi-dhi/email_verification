from student.models import Student
from student.serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .permissions import IsAdministrationOrTeacher
from .permissions import IsAdministration
from classroom.models import Classroom
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.utils import timezone
from .paginations import CustomPagination

class StudentListGetApi(APIView):
    def get(self, request):
        student = Student.objects.select_related('user','class_enrolled').all() 
        # student = Student.objects.all()
        # student = Student.objects.prefetch_related('class_enrolled').filter(class_enrolled = 1)
        paginator = CustomPagination()
        result = paginator.paginate_queryset(student, request)
        serializer = StudentSerializer(result, many= True)
        return paginator.get_paginated_response(serializer.data)
        # return Response(serializer.data)

class StudentDetailGetApi(APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk = pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response({"detail":"Student not found"}, status= status.HTTP_404_NOT_FOUND)

class StudentDetailUpdateApi(APIView):
    permission_classes=[IsAdministrationOrTeacher]
    def post(self, request, pk):
        student = Student.objects.filter(pk = pk, is_deleted = False).last()
        serializer= StudentSerializer(student, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class StudentDetailDeleteApi(APIView):
    permission_classes=[IsAdministration]
    def delete(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        student.is_deleted = True
        student.save()
        return Response(status= status.HTTP_204_NO_CONTENT)
