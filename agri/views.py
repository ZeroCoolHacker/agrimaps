from django.shortcuts import render
from .models import Faculty, Department

# Create your views here.
def home(request):
    faculties   = Faculty.objects.all()
    departments = Department.objects.all()
    context     = {
        'faculties': faculties,
        'departments': departments,
    }
    return render(request, 'agri/home.html', context=context)


def department(request, pk):
    return render(request, 'agri/department.html', {'pk':pk})