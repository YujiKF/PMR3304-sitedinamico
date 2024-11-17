from django.shortcuts import render

def home(request):
    return render(request, 'staticpages/home.html')

def about(request):
    return render(request, 'staticpages/about.html')