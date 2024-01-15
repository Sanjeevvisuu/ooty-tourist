from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def about_us(request):
    return render(request,"about_us.html")
def package(request):
    return render(request,"package.html")
def home(request):
    return render(request,"home.html")