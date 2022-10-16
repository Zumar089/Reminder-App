from django.shortcuts import render,HttpResponse

# Create your views here.

def homepage(request):
    return render(request,"home.html")

def createReminder(request):
    return render(request,"create.html")

def calender(request):
    return render(request,"calender.html")

def time_note(request):
    return render(request,"timenote.html")