from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(request):
    return HttpResponse("<h2>Good Morning user..!! Have a Nice Day...</h2><hr/>");
def f2(request):    
    return HttpResponse("<h2>Good Afternoon User..!! Have a Nice Day...</h2><hr/>");
def f3(request):
    return HttpResponse("<h2>Good Evening User..!! Have a Nice Day...</h2><hr/>");