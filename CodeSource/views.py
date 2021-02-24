from django.shortcuts import render

def index(request):
    return render(request,'CodeSource/Home.html')
	
def home(request):
    return render(request,'CodeSource/Home.html')

def about(request):
    return render(request,'CodeSource/About.html')

def projects(request):
    return render(request,'CodeSource/Projects.html')

def videos(request):
    return render(request,'CodeSource/Videos.html')
