from django.shortcuts import render
from .models import Student

# Create your views here.
def index(req):
   student = Student.objects.all()
   context = {'student':student}
   return render(req, 'index.html',context)

def studentdetails(req , student_id):
   studentrecord = Student.objects.get(student_id = student_id)
   context ={'studentrecord' : studentrecord }
   return render(req , "studentdetails.html" ,context)

   