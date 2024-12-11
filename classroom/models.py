from django.db import models

class Classroom(models.Model):
    room_number = models.CharField(max_length=10)
    total_seat = models.CharField(max_length = 5, null=True, blank = True)     
    is_deleted = models.BooleanField(default=False)
    class Meta:
        db_table ='CLASSROOM'
    def __str__(self):
        return self.room_number
    