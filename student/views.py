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

class StudentListGetApi(APIView):
    @method_decorator(cache_page(60*15))
    # @cache_page(60*60)
    def get(self, request):
        # start_time = timezone.now()

        student = Student.objects.select_related('user','class_enrolled').all() 
        # student = Student.objects.all()
        # student = Student.objects.prefetch_related('class_enrolled').filter(class_enrolled = 1)
        serializer = StudentSerializer(student, many= True)
        # end_time = timezone.now()
        # elapsed_time = end_time - start_time
        # Time= elapsed_time.total_seconds()
        # print(Time)

        return Response(serializer.data)

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
