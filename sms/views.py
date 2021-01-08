#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
from models import *
from django.db import connection
# Create your views here.
from sms.models import *

def input_base_info(request):
    return render(request, 'index.html')


# def base_submit(request):
#     course = request.POST.get('q1', None)
#     name = request.POST.get('q2', None)
#     company_name = request.POST.get('q3', None)
#     salary = request.POST.get('q4', None)
#     phone = request.POST.get('q5', None)
#     flag = 1
#     if course and name and company_name and salary and phone:
#         if phone.isdigit and len(phone) == 11:
#             if Student.objects.filter(phone=phone).exists():
#                 try:
#                     salary = int(salary)
#                 except:
#                     salary = 0
#
#                 try:
#                     Student.objects.create(name=name,
#                                            company_name=company_name,
#                                            phone=phone,
#                                            salary=int(salary))
#                     flag = 0
#                     message = u'存储成功'
#                 except:
#                     message = u'服务器断开'
#             else:
#                 message = u'手机号已存在，无法重复提交'
#         else:
#             message = u'手机号不合法'
#     else:
#         message = u'缺少必填参数'
#
#     # return HttpResponse('1')
#     data = {'message': message, 'flag': flag}
# #
#     return render(request, 'result.html', {'data': json.dumps(data)})


def base_submit(request):

    course = request.POST.get('q1', None)
    name = request.POST.get('q2', None)
    company = request.POST.get('q3', None)
    salary = request.POST.get('q4', None)
    phone = request.POST.get('q5', None)
    if course and name and company and salary and phone:
        courses = course.split('a')
        base = []
        perfromce = []
        automation = []
        develop = []
        course_data = []
        for i in range(len(courses) - 1):
            if courses[i].strip().startswith(u'1_'):
                base.append(courses[i])
            elif courses[i].strip().startswith(u'2_'):
                base.append(courses[i])
            elif courses[i].strip().startswith(u'3_'):
                base.append(courses[i])
            elif courses[i].strip().startswith(u'4_'):
                base.append(courses[i])
            if len(base) > 0:
                d = base[-1]
                course_data['1'] = d[d.index('_') + 1:]
            if len(perfromce) > 0:
                d = perfromce[-1]
                course_data['2'] = d[d.index('_') + 1:]
            if len(automation) > 0:
                d = automation[-1]
                course_data['3'] = d[d.index('_') + 1:]
            if len(develop) > 0:
                d = develop[-1]
                course_data['4'] = d[d.index('_') + 1:]


            if phone.isdigit():
                if not Student.objects.filter(phone=phone).exists():
                    # try:
                    #     salary = int(salary)
                    # except:
                    #     salary = 0
                    student = Student.objects.create(name=name,
                                                     company=company,
                                                     phone=phone,
                                                     salary=int(salary))
                    for c_id, c_qi in course_data.items():
                        try:
                            co = Course.objects.get(id=id)
                            co.student.add(student)
                            cursor = connection.cursor()
                            sql = "update sms_course_stduent set semester=%s WHERE course_id=%s AND student_id=%s" % (c_qi, c_id, student.id)
                            cursor.execute(sql)
                            message = u' '
                            flag = 0
                        except Exception as e:
                            print e
                            message = u'数据存储错误'
                            flag = 1
                else:
                    message = u'手机号已存在，无法再次提交'
                    flag = 1
            else:
                message = u'手机号格式错误'
                flag = 1
        else:
            message = u'信息不完整'
            flag = 1
        data = {'message': message, 'flag': flag}
        return render(request, 'result.html', {'data': json.dumps(data)})