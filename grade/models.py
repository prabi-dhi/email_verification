from django.db import models
from student.models import Student
from subject.models import Subject

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    grade = models.CharField(max_length=5)
    is_deleted = models.BooleanField(default = False)

    class Meta:
        db_table = 'GRADE'
    
    def __str__(self):
        return self.student

