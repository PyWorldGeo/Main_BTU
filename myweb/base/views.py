from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, User, Author, Genre
from django.db.models import Q

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    #books = Book.objects.filter(genre__name__icontains=q) #i means insencitive to lower/high cases
    books = Book.objects.filter(Q(genre__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    #books = Book.objects.all()
    books = list(set(books))
    genres = Genre.objects.all()
    heading = "Library"
    context = {"books": books, "genres": genres, 'heading': heading}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')


# def profile(request):
#     user = User.objects.get(id=1)
#     books = user.books.all()
#
#     context = {"books": books}
#     return render(request, 'base/profile.html', context)

def profile(request, pk):
    user = User.objects.get(id=pk)
    # books = user.books.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    books = user.books.filter(Q(genre__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    books = list(set(books))
    genres = Genre.objects.all()
    heading = 'My Books'
    context = {"books": books, "user": user, 'genres': genres, 'heading': heading}
    return render(request, 'base/profile.html', context)


def reading(request, file):
    return render(request, 'base/reading.html', {'file': file})