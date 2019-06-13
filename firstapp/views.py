from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework import viewsets
from .serializers import UserSerializer, ArticleSerializer


def home(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'firstapp/home.html', context)


def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {'user':user}
    return render(request, 'firstapp/profile.html', context)


def login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'firstapp/login.html', {'form':form})


def register(request):
    if request.method=='POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
        context = {'form':form}
        return render(request, 'firstapp/register.html', context)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
