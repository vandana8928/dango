from django.http import HttpResponse
from django.shortcuts import render


def mainpage(request):
    data={
        'title':'Home page'
    }
    return render(request,"index.html",data)

def home(request):
    return HttpResponse("vandana yadav")
