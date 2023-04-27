from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'my_app/index.html')

def employeeView(request):
    employee = {
        'id':123,
        'name': "Mustang",
        "salary": 1900000,
    }
    return JsonResponse(employee)