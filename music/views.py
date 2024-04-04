from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from pymongo.auth import authenticate, logout

from .models import Genre
from .models import Music
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MusicForm

from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicForm
from .models import Genre, Music

def index(request):
    latest_genres = Genre.objects.all()[:3]
    return render(request, 'index.html', {'latest_genres': latest_genres})


def muz_all(request):
    genres = Genre.objects.all()
    return render(request, 'muz_all.html', {'genres': genres})


from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from .forms import MusicForm
from .models import Genre

# views.py

from django.shortcuts import render, redirect
from .forms import MusicForm  # Импортируем форму для добавления музыки
from .models import Genre  # Импортируем модель Genre для получения списка жанров

def add_muz(request):
    genres = Genre.objects.all()
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)
            music.genre = Genre.objects.get(pk=request.POST['genre'])
            music.save()
            return redirect('index')
    else:
        form = MusicForm()

    return render(request, 'add_muz.html', {'form': form, 'genres': genres})


def update_music(request, song_id):
    song = get_object_or_404(Music, pk=song_id)
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MusicForm(instance=song)
    return render(request, 'update_music.html', {'form': form})


# views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Music


def delete_music(request, song_id):
    news = get_object_or_404(Music, id=song_id)
    news.delete()
    return redirect('index')


def list_genres(request):
    genres = Genre.objects.all()
    return render(request, 'list_genres.html', {'genres': genres})


from django.shortcuts import render, get_object_or_404
from .models import Genre, Music

def view_music(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    music = Music.objects.filter(genre=genre)
    return render(request, 'view_music.html', {'genre': genre, 'music': music})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')  # замените 'home' на имя вашего представления для домашней страницы
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')  # замените 'home' на имя вашего представления для домашней страницы
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('index')  # замените 'home' на имя вашего представления для домашней страницы

