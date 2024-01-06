from django.shortcuts import render , redirect , get_object_or_404
from .models import Student
from .forms import RegisterStudent

# Create your views here.
def index(req):
   student = Student.objects.all()
   context = {'student':student}
   return render(req, 'index.html',context)

def studentdetails(req , student_id):
   studentrecord = Student.objects.get(student_id = student_id)
   context ={'studentrecord' : studentrecord }
   return render(req , "studentdetails.html" ,context)

def delete_student(req,student_id):
    studentrecord = Student.objects.get(student_id = student_id)
    studentrecord.delete()
    return redirect('/')

def register_student(req):
   if req.method == "GET":
      context={}
      form =RegisterStudent()
      context['form']=form 
      return render(req,'register_student.html' ,context)
   else:
      context={}
      form = RegisterStudent(req.POST,req.FILES or None)
      if form.is_valid():
         form.save()
      context['form']= form
      return redirect("/")
