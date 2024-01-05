from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(primary_key = True)
    student_name = models.CharField(max_length = 20)
    gender_choice =(("male","male"),("female","female"))
    gender = models.CharField(choices=gender_choice,default = "",max_length=6) #radio button 
    dob =models.DateField(default="")
    student_image = models.ImageField(upload_to="images")
    address = models.TextField()
    grade = models.CharField(max_length=2) 

