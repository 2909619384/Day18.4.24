from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import Student


def addStudent(request):
    print(request)
    stu = Student()
    stu.name = '张三'
    stu.sex = 1
    stu.save()

    return HttpResponse('添加成功')