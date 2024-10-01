from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Person, Student, Teacher

# Create your views here.
class person_list(ListView):
    model = Person
    template_name = 'person_list.html'

class student_list(ListView):
    model = Student
    template_name = 'student_list.html'

class teacher_list(ListView):
    model = Teacher
    template_name = 'teacher_list.html'