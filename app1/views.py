from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('<button> MSD is Best Wicket Keeper and Finisher </button>')