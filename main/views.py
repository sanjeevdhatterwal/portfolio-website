from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    response=render(request,'main/index.html',context)
    return response
def projects(request):
    context={}
    response=render(request,'main/projects.html',context)
    return response
def languages(request):
    context={}
    response=render(request,'main/languages.html',context)
    return response