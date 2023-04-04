from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# HttpResponse에 커서 클릭하고 Alt + Enter 누른 다음 import구문 클릭
def hello_world(request):
    return HttpResponse('Hello world!')