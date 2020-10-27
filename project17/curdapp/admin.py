from django.contrib import admin
from curdapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    '''
        Admin View for Student
    '''
    list_display = ('student_name','student_phone_no','student_mail_id','student_address')
    

admin.site.register(Student, StudentAdmin)