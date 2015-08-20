from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def hello(request):
    print 'test git in pycharm'
    print 'test git in pycharm again'
    return HttpResponse('Hello world!')
#endof hello(request)