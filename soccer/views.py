from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def contact(request):
     return render(request,"contact.html")
def blog(request):
     return render(request,"blog.html")
def matches(request):
     return render(request,"matches.html")
def players(request):
     return render(request,"players.html")
def single(request):
     return render(request,"single.html")
def main(request):
     return render(request,"main.html")