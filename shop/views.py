from django.shortcuts import render , HttpResponse  

def hi(request):
    return render(request,'index.html',{})