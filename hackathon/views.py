
from django.shortcuts import render
from django.template.context import RequestContext
shortlist = {}


def index(request):
    return render(request, 'index.html')


def destinations(request):
    return render(request, 'destinations.html')



def now(request):
    return render(request, 'now.html')


def after(request):
    return render(request, 'after.html')


def shortlisted(request):
    return render(request, 'shortlisted.html',shortlist)


def guidelines(request):
    return render(request, 'guidelines.html')

def sign(request):
    return render(request,'sign.html')
