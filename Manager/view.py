# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

def manager(request):
    context = {}
    context['manager'] = 'Score Manager'
    return render(request, 'manager.html', context)