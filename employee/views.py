from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def employee(request):
    return HttpResponse("THIS IS sadasdasd")
def profile(request):
    return render(request,'employee/profile.html')
