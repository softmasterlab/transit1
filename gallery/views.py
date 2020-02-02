from django.shortcuts import render


def index(request):
    return render(request, 'gallery/index.html')


def add(request):
    return render(request, 'gallery/add.html')


def delete(request):
    return render(request, 'gallery/delete.html')
