from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def client(request):
    return render(request, 'clientPage.html')

def doctor(request):
    return render(request, 'doctorPage.html')