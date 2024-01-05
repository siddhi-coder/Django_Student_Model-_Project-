from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 
                    'student_name',
                    'gender','dob',
                    'student_image',
                    'address',
                    'grade')
admin.site.register(Student,StudentAdmin)


