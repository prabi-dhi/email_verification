from django.db import models
from user.models import User

class Teacher(models.Model):
    teacher_name = models.CharField(max_length = 50)
    # department = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null =True, blank = True)
    
    class Meta:
        db_table = 'TEACHER'
        
    def __str__(self):
        return self.name
