from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def one(request):
    s="i love india"
    return HttpResponse(s)