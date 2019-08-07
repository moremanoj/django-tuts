from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import UserRegisterForm, ServiceBookingForm
from django.contrib import messages

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def Home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

def About(request):
    return render(request, 'about.html')

def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('garage-home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def Login(request):
    return render(request, 'login.html')

def History(request):
    return render(request, 'history.html')

def Service(request):
    if request.method == 'POST':
        form = ServiceBookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully registered !')
            return redirect('garage-history')
    else:
        form = ServiceBookingForm()
    return render(request, 'book-service.html', {'form': form})

def AdminCalender(request):
    return render(request, 'admin-calender.html')