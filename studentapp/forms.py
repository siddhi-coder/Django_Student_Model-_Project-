from studentapp.models import Student
from django.forms import ModelForm

class RegisterStudent(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        