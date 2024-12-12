from rest_framework.views import APIView
from .models import Grade
from .serializers import GradeSerializer
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAuthenticatedTeacher

class GradeListApi(APIView):
    def get(self, request):
        grade = Grade.objects.all()
        serializer = GradeSerializer(grade, many=True)
        return Response(serializer.data)
    
class GradeAddApi(APIView):
    permission_classes=[IsAuthenticatedTeacher]
    def post(self, request):
        serializer = GradeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class GradeDetailGetApi(APIView):
    def get(self, request, pk):
        grade = Grade.objects.filter(pk=pk, is_deleted = False).last()
        serializer = GradeSerializer(grade)
        return Response(serializer.data)
    
class GradeDetailUpdateApi(APIView):
    permission_classes=[IsAuthenticatedTeacher]
    def post(self, request, pk):
        grade = Grade.objects.filter(pk=pk, is_deleted = False).last()
        serializer = GradeSerializer(grade, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GradeDetailDeleteApi(APIView):
    permission_classes=[IsAuthenticatedTeacher]
    def delete(self, request, pk):
        grade = Grade.objects.filter(pk=pk, is_deletd = False).last()
        grade.is_deleted = True
        grade.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
