from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import Person, Student, Teacher

# Create your views here.
class person_list(ListView):
    model = Person

class student_list(ListView):
    model = Student
    template_name = 'student_list.html'

class teacher_list(ListView):
    model = Teacher
    template_name = 'teacher_list.html'

class person_list_context(TemplateView):

    template_name = "person_list.html"

    extra_context={'object_list': Person.objects.all()}

class person_student(person_list_context):

    template_name = "student_list.html"

    extra_context={'object_list': Student.objects.all()}

class person_teacher(person_list_context):

    template_name = "teacher_list.html"

    extra_context={'object_list': Teacher.objects.all()}