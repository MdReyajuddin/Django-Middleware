from django.shortcuts import render

# Create your views here.

def home(request):
    # s=10/0
    return render(request, 'home.html')
