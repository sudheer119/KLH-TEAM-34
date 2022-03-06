from http.client import HTTPResponse
from pyexpat import model
from re import template
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import code


# ML IMPORTS


# class HomeView(TemplateView):
#     template_name = 'home/welcome.html'
#     today = {'today': datetime.today()}

def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})


# @login_required(login_url='/admin')
# def author(request):
#     return render(request, 'home/auhtor.html', {})
class Author(LoginRequiredMixin, TemplateView):
    template_name = 'home/author.html'
    login_url = '/admin'


# ML CODE #.......................................................................................


def add(request):
    val1 = request.GET["num1"]
    val2 = request.GET["num2"]
    val3 = request.GET["num3"]
    val4 = request.GET["num4"]
    val5 = request.GET["num5"]
    res = code.cal(val1, val2, val3, val4, val5)
    return render(request, 'home/welcome.html', {"sum": res})
