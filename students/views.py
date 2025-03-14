from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# 📌 Create Student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# 📌 Read - List Students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# 📌 Update Student
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

# 📌 Delete Student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect('student_list')
