from django.db import models
from user.models import User
from classroom.models import Classroom

class Student(models.Model):
    student_name = models.CharField(max_length = 50)
    class_enrolled = models.ForeignKey(Classroom, on_delete=models.CASCADE, null= True, blank = True)
    is_deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null= True, blank =True)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return self.student_name
    
    # def save(self, *args, **kwargs):
    #     if self.user_type == User.Types.STUDENT:
    #         if not hasattr(self, 'student'): 
    #             student = Student.objects.create(user=self)
    #     super().save(*args, **kwargs)