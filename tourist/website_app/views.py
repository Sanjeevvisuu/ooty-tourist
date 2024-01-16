from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"welcome/index.html")
def product(request):
    return render(request,"product/index.html")
def booking(request):
    return render(request,"booking/index.html")