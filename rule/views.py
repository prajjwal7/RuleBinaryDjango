from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request , "index.html")
def O1Olive(request) :
    return render(request , "01Olive.html")