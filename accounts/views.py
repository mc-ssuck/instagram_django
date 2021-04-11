from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from posts import forms

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    
    return redirect('accounts:login')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def profile(request, pk):
    User = get_user_model()
    user_info = User.objects.get(pk=pk)
    form = forms.CommentForm

    context = {
        'user_info': user_info,
        'form' : form,
    }

    return render(request, 'accounts/profile.html', context)

def follow(request, pk):
    you = get_object_or_404(get_user_model(), pk=pk)
    me = request.user

    if me == you:
        return('accounts:profile', pk)

    if me in you.followers.all():
    # if you in me.followings.all()
        you.followers.remove(me)
    else:
        you.followers.add(me)
    
    return redirect('accounts:profile', pk)

