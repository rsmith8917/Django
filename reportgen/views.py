from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'':''}
    return render(request, 'index.html', context_dict)

def report(request):
    context_dict = {'title':'My Report!','time':'now'}
    return render(request, 'report.html', context_dict)
