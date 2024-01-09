from django.forms import PasswordInput
from django.shortcuts import render , redirect , get_object_or_404
from .models import Student
from .forms import RegisterStudent
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout


# Create your views here.
def index(req):
   if req.user.is_authenticated:   
    username = req.user 
    student = Student.objects.all()
    context = {'student':student , "username" : username}
    return render(req, 'index.html',context)
   else:
    student = Student.objects.all()
    context = {'student':student ,}
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

def edit_student(req, student_id):
    studentrecord = Student.objects.get(student_id=student_id)
    if req.method == "POST":
        form = RegisterStudent(req.POST, req.FILES, instance=studentrecord)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterStudent(instance=studentrecord)
    context = {
        "form": form,
        "studentrecord": studentrecord
    }
    return render(req, "edit_student.html", context)

def signup(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        passwd = req.POST["passwd"]
        cpasswd = req.POST["cpasswd"]
        context = {}
        if uname == "" or passwd == "" or cpasswd == "":
            context['errormessage'] = "Field can't be empty"
            return render(req,"signup.html" , context)
        elif passwd != cpasswd :
            context['errormessage'] ="Password doesn't match"
            return render(req,"signup.html" , context)
        else:
            try:
                # Create the user if everything is fine
                userdata = User.objects.create(username=uname, password=passwd)
                userdata.set_password(passwd)
                userdata.save()
                return redirect("/")
            except:
                context["errormessage"] = "User Already exists"
                return render(req, "signup.html" , context)
    else:
        return render(req, "signup.html")
def signin(req):
    if req.method == "POST":  # Corrected method to lowercase "post"
        uname = req.POST.get("uname")
        passwd = req.POST.get("passwd")
        context = {}
        if not (uname and passwd):
            context['errormessage'] = "Fields can't be empty"
            return render(req, "signin.html", context)
        else:
            userdata = authenticate(username=uname, password=passwd)
            if userdata is not None:
                login(req, userdata)
                return redirect("/")
            else:
                context['errormessage'] = "Invalid username or password"
                return render(req, "signin.html", context)
    else:
        return render(req, "signin.html")
        


       