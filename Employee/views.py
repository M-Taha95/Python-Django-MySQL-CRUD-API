from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departments, Employees
from .serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == "GET":
        department = Departments.objects.all()
        departments_serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == "POST":
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Succressfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(
            DepartmentId=department_data["DepartmentId"]
        )
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Faild to Update")
    elif request.method == "DELETE":
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully")


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == "GET":
        employee = Employees.objects.all()
        employee_seializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_seializer.data, safe=False)
    elif request.method == "POST":
        employee_data = JSONParser().parse(request)
        employee_seializer = EmployeeSerializer(data=employee_data)
        if employee_seializer.is_valid():
            employee_seializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Faild Added!", safe=False)
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data["EmployeeId"])
        employee_seializer = EmployeeSerializer(employee, data=employee_data)
        if employee_seializer.is_valid():
            employee_seializer.save()
            return JsonResponse("Update Successfully!", safe=False)
        return JsonResponse("Faild Update!", safe=False)
    elif request.method == "DELETE":
        employee = Employees().objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleting Sucessfully!", safe=False)


@csrf_exempt
def SaveFile(requset):
    file = requset.FILES["file"]
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
