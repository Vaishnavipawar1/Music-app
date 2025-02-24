from django.shortcuts import render
from musicbeats.models import Song

def index(request):
    song = Song.objects.all()
    return render(request,'index.html', {'song': song})

def songs(request):
    song = Song.objects.all()
    return render('musicbeats/songs.html')

def basic_view(request):
    song = Song.objects.all()
    return render(request, 'musicbeats/basic.html')

def basic_view(request):
    song = Song.objects.all()
    return render(request, 'musicbeats/signup.html')

def basic_view(request):
    song = Song.objects.all()
    return render(request, 'musicbeats/login.html')