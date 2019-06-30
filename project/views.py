from django.shortcuts import render, redirect, get_object_or_404
from posts .models import Post, Galery
from posts import views


def home(request):
    galery = Galery.objects.all()
    return render(request, 'home.html', {"galery": galery})
