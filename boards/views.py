# -*- coding: utf-8 -*-
# boards/views.py
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})