from django.shortcuts import render
from django.http import HttpResponse
from .models import Account,Invoice,InvoiceLineItem

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

