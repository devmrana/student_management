from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student
from .forms import *

# List Students
class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

# Create Student (CBV)
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, "Student added successfully!")
        return super().form_valid(form)

# Update Student (CBV)
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, "Student updated successfully!")
        return super().form_valid(form)

# Delete Student (CBV)
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'  # Create this template
    success_url = reverse_lazy('student_list')

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, "Student deleted successfully!")
        return super().delete(request, *args, **kwargs)
