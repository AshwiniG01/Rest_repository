from django.db import models

# Create your models here.
class Student(models.Model):
	student_name = models.CharField(max_length=50)
	student_phone_no = models.IntegerField()
	student_mail_id = models.CharField(max_length=50)
	student_address = models.CharField(max_length=50)
