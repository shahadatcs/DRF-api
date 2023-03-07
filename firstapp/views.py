from django.shortcuts import render
from django.http import JsonResponse
from . models import employee
# Create your views here.
def employeeView(request):
    
    emp={
        'name': 'Shahadat',
        'sal': 10000,
        'id': 100
    }
    
    data = employee.objects.all()
    response = {'employees': list(data.values('id', 'name', 'sal'))}
    
    return JsonResponse(response)