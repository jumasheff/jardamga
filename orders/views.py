from django.shortcuts import render


def index(request):
    template = 'orders/index.html'
    return render(request, template)
