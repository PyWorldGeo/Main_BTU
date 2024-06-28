from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, User, Author, Genre
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MyUserCreationForm

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
    print(books[0].users.all())
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def about(request):
    return render(request, 'base/about.html')


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


def reading(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'base/reading.html', {'book': book})

def adding(request, id):
    book = Book.objects.get(id=id)
    user = request.user
    user.books.add(book)

    return redirect('home')





def login_page(request):
    #ბოლოს
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist!")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password doesn't exist!")

    context = {"page": page}
    return render(request, "base/login_register.html", context)



def delete(request, pk):
    book = Book.objects.get(id=pk)

    # if request.user != room.host:
    #     return HttpResponse("<h1>You Don't Have Permission!</h1>")

    if request.method == "POST":
        request.user.books.remove(book)
        return redirect('profile', request.user.id)
    return render(request, 'base/delete.html', {'obj': book})


def logout_user(request):
    logout(request)
    return redirect('home')

def register_page(request):
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration")

    return render(request, 'base/login_register.html', {'form': form})