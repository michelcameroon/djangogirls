
from django.shortcuts import render, get_object_or_404
# Create your views here.

#from django.shortcuts import render
from django.utils import timezone
from .models import Students

from .forms import StudentsForm

from django.shortcuts import redirect



def students_list(request):
    studentss = Students.objects.all()
    return render(request, 'students/students_list.html', {'studentss': studentss})



def students_new(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            students = form.save(commit=False)
            '''
            #post.author = request.user
            '''
            students.created_date = timezone.now()
            students.save()
            return redirect('students_detail', pk=students.pk)
    else:
        form = StudentsForm()
    return render(request, 'students/students_edit.html', {'form': form})




def students_detail(request, pk):
    students = get_object_or_404(Students, pk=pk)
    return render(request, 'students/students_detail.html', {'students': students})


def students_edit(request, pk):
    students = get_object_or_404(Students, pk=pk)
    if request.method == "POST":
        form = StudentsForm(request.POST, instance=students)
        if form.is_valid():
            students = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            students.save()
            return redirect('students_detail', pk=students.pk)
    else:
        form = StudentsForm(instance=students)
    return render(request, 'students/students_edit.html', {'form': form})


