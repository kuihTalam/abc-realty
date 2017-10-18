# -*- coding: utf-8 -*-
# boards/views.py
from __future__ import unicode_literals

from django.http import HttpResponse
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})