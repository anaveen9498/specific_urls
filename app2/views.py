from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def virat(request):
    return HttpResponse('<h1><marquee> virat bhai is best cricket player in the world</marquee></h1>')