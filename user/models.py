from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid
from django.apps import apps
# from student.models import Student

class User(AbstractUser):
    class Types(models.TextChoices):
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"
        ADMINISTRATION = "ADMINISTRATION", "Administration"
    user_type = models.CharField(max_length=20, choices=Types.choices, default=Types.STUDENT)
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255,unique=True)
    is_deleted = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default= False)
    
    class Meta:
        db_table = 'users'
        
    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs) 
            if self.user_type == self.Types.STUDENT:
                Student = apps.get_model('student', 'Student')
                Student.objects.create(user=self, student_name=self.username)
            elif self.user_type == self.Types.TEACHER:
                Teacher = apps.get_model('teacher', 'Teacher')
                Teacher.objects.create(user=self, teacher_name=self.username)
        else:
            super().save(*args, **kwargs)

class VerificationToken(models.Model):
    user = models.ForeignKey(User, related_name='verification_tokens', on_delete=models.CASCADE, null= True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        # return f"{self.user.username}"
        return {self.user.username}
    
    class Meta:
        db_table = 'tokens'