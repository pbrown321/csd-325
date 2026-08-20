from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Phil says Hello")


