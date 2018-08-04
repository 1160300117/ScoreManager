from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .form import SearchStudentForm, SearchScoreForm, SearchSubjectForm, AddForm, ChangeForm, DeleteForm
import os
from . import manager

def add(request):
    key = ""
    request.encoding='utf-8'
    key = request.GET['add']
    return render(request, "add.html", {'add': manager.add(key)})

def change(request):
    key = ""
    request.encoding='utf-8'
    key = request.GET['change']
    return render(request, "change.html", {'change': manager.change(key)})


def delete(request):
    key = ""
    request.encoding='utf-8'
    key = request.GET['delete']
    return render(request, "delete.html", {'delete': manager.delete(key)})

def search_student(request):
    key = ""
    request.encoding='utf-8'
    key = request.GET['student']
    return render(request, "search_student.html", {'search_student': manager.search_student(key)})

def search_subject(request):
    key = ""
    request.encoding='utf-8'
    key = request.GET['subject']
    response = manager.search_subject(key)
    return render_to_response('search_subject.html',{'search_subject': response})

def search_score(request):
    key = 100
    request.encoding='utf-8'
    key = float(request.GET['score'])
    response = manager.search_score(key)
    return render_to_response('search_score.html',{'search_score': response})