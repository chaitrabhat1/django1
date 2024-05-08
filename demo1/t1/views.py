from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def t1(request):
    template=loader.get_template('page.html')
    return HttpResponse()
# Create your views here.
