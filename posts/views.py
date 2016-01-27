#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nabi'

from django.http import HttpResponse
from django.shortcuts import render

def post_home(request):
    return HttpResponse("<H1> Hello~! The First~!</h1>")

