from django.shortcuts import render, HttpResponse 

# Create your views here.
def home(request):
    context = {'name':'Sakshi', 'course':'django'}
    return render(request, 'home.html',context)

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')
