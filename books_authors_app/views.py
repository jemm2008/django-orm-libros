from django.shortcuts import render, HttpResponse

def index2(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)

