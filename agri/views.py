from django.shortcuts import render
from .models import Faculty, Department, vips

# Create your views here.
def home(request):
    faculties   = Faculty.objects.all()
    departments = Department.objects.all()
    context     = {
        'faculties': faculties,
        'departments': departments,
    }
    return render(request, 'agri/testhome.html', context=context)


def department(request, pk):
    department = Department.objects.get(pk=pk)
    return render(request, 'agri/department.html', {'department':department})


def info(request):
    vip = vips.objects.all()
    return render(request, 'agri/info.html', {'vips':vip})