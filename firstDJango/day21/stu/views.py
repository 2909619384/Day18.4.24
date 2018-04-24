from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from stu.models import Student


def addStu(request):

    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':

        print(request)
        print(request.POST)
        stu_name = request.POST.get('name')
        if request.POST.get('sex') == '男':
            stu_sex = 1
        else:
            stu_sex = 0
        stu_birth = request.POST.get('birth')
        stu_tel = request.POST.get('tel')

        stu = Student()
        stu.stu_name = stu_name
        stu.stu_birth = stu_birth
        stu.stu_sex = stu_sex
        stu.stu_tel = stu_tel
        stu.save()

        # Student.objects.create(
        #     stu_name == stu_name,
        #     stu_birth == stu_birth,
        #     stu_sex == stu_sex,
        #     stu_tel == stu_tel
        # )
        return HttpResponse('添加学生信息成功')

def selectStu(request):

    stus = Student.objects.all()

    #查询所有女生的信息
    # stus = Student.objects.filter(stu_sex=False)
    # stus = Student.objects.get(stu_name=False)
    #查询id从大到小，从小到大去掉减号
    # stus = Student.objects.all().order_by('-id')
    #获取ID最大的一条数据
    stus = Student.objects.all().order_by('-id').first()
    # stus = Student.objects.all().order_by('-id').last()
    #获取男生的数据的个数
    # stus = Student.objects.filter(stu_sex=True).count()

    #查询所有80后女生的信息
    # stus = Student.objects.filter(stu_sex=False,
    #                               stu_birth__gte='1980-01-01',
    #                               stu_birth__lte='1990-01-01')
    #查询姓李的数据
    # stus = Student.objects.filter(stu_name__startswith='李')
    #查询以花结束的数据
    # stus = Student.objects.filter(stu_name__endswith='花')


    #姓名中包含李的数据
    # stus = Student.objects.filter(stu_name__contains='李')

    #判断一个姓名是否存在
    # stus = Student.objects.filter(stu_name='cc').exists()

    # #获取指定多个id的值
    # ids = [1,4]
    # stus = Student.objects.filter(id__in=(ids))

    #查询语文成绩大于等于数学成绩的学生
    stus = Student.objects.filter(stu_yuwen__gte=F('stu_shuxue'))

    #  查询语文成绩大于等于数学10分成绩的学生

    # stus = Student.objects.filter(stu_yuwen__gte=F('stu_shuxue')+10)

    #查询学生姓名不叫李白的，或者语文成绩大于80分的学生
    stus = Student.objects.filter(~Q(stu_name='李白') | Q(stu_yuwen__gt=80))



    # return render(request, 'detail.html', {'stus': stus})
    return render(request, 'sel_stu.html', {'stus': stus})


