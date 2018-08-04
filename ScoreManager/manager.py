# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from ScoreManager.models import Student

def search_subject(key):
    list = []
    students = {}
    for student in Student.objects.all():
        if key == 'chinese':
            students[student] = student.chinese
            list.append(student.chinese)
        elif key == 'math':
            students[student] = student.math
            list.append(student.math)
        elif key == 'english':
            students[student] = student.english
            list.append(student.english)
        elif key == 'physics':
            students[student] = student.physics
            list.append(student.physics)
        elif key == 'chemistry':
            students[student] = student.chemistry
            list.append(student.chemistry)
        elif key == 'summary':
            students[student] = student.summary
            list.append(student.summary)
    list.sort(reverse=True)
    response = []
    r = ""
    for l in list:
        for student in students.keys():
            if students[student] == l:
                r = student.number + " " + student.name + " " + key + ": " + str(l)
                response.append(r)
    return response

def search_score(key):
    students = []
    list = []
    for student in Student.objects.all():
        if student.chinese >= key and student.math >= key and student.english >= key and student.physics >= key and student.chemistry >= key:
            students.append(student)
            list.append(student.summary)
    list.sort(reverse=True)
    response = []
    r = ""
    for l in list:
        for student in students:
            if student.summary == l:
                r = student.number + " " + student.name + " chinese:" + str(student.chinese) + " math:" + str(student.math) + " english:" + str(student.english) + " physics" + str(student.physics) + " chemistry:" + str(student.chemistry)+ " summary:" + str(l)
                response.append(r)
    return response

def search_student(key):
    response = ""
    for student in Student.objects.all():
        if student.number == key or student.name == key:
            response = student.number + " " + student.name + " chinese:" + str(student.chinese) + " math:" + str(student.math) + " english:" + str(student.english) + " physics" + str(student.physics) + " chemistry:" + str(student.chemistry)+ " summary" + str(student.summary)
    return response

def add(key):
    keys = key.split()
    if len(keys) != 8:
        return "输入信息错误"
    else:
        find = False
        for student in Student.objects.all():
            if student.number == keys[0]:
                return "该学生已存在"
        if not find:
            student = Student(number=keys[0], name=keys[1], chinese=float(keys[2]), math=float(keys[3]), english=float(keys[4]), physics=float(keys[5]), chemistry=float(keys[6]), summary=float(keys[7]))
            student.save()
            return "添加信息成功"

def change(key):
    keys = key.split()
    if len(keys) != 8:
        return "输入信息错误"
    else:
        find = False
        for student in Student.objects.all():
            if student.number == keys[0] or student.name == keys[1]:
                find = True
                student.number = keys[0]
                student.name = keys[1]
                student.chinese = float(keys[2])
                student.math = float(keys[3])
                student.english = float(keys[4])
                student.physics = float(keys[5])
                student.chemistry = float(keys[6])
                student.summary = float(keys[7])
                student.save()
                return "修改信息成功"
        if not find:
            return "该学生不存在"

def delete(key):
    find = False
    for student in Student.objects.all():
        if student.number == key or student.name == key:
            find = True
            student.delete()
            return "删除信息成功"
    if not find:
        return "该学生不存在"