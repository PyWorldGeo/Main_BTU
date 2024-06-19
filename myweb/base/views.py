from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, User, Author


# Create your views here.
def home(request):
    books = Book.objects.all()
    context = {"books": books}
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
    books = user.books.all()
    context = {"books": books, "user": user}
    return render(request, 'base/profile.html', context)