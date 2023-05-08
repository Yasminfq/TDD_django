from django.shortcuts import render

# Create your views here.
def minha_func(request):
    return render(request, 'index.html')
