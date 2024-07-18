from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def agent(request):
    return render(request,'agents-grid.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog-single.html')
def property(request):
    return render(request,'property-grid.html')
def singlepage(request):
    return render(request,'property-single.html')
def grid(request):
    return render(request,'blog-grid.html')
def agents(request):
    return render(request,'agent-single.html')