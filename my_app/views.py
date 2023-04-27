from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
# Create your views here.

def index(request):
    return render(request, 'my_app/index.html')

def employeeView(request):
    data = Employee.objects.all()
    response = {'employee':list(data.values('id','name','salary'))}
    return JsonResponse(response)