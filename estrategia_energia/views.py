from django.shortcuts import render


def home(request):
    return render(request, 'estrategia_energia/index.html')