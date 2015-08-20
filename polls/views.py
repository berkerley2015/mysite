from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print 'test git in pycharm'
    print 'test git in pycharm again'
    return HttpResponse('Hello world!')
#endof index(request)

#conventional arguments coding style **/?first=9&second=8
def sum(request):
    first = request.GET['first']
    second = request.GET['second']
    sumup = int(first) + int(second)
    return HttpResponse(str(sumup))
#endof sum(request)

#arguments coding style confirms to the **/**/**
def sum2(request,first,second):
    sum = int(first) + int(second)
    return HttpResponse(str(sum))
#endof sum2(request,first,second)

#test template
def home(request):
    return render(request,'home.html')
#endof home(request)





















