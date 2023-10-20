from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import User
from boards.models import Board, Comment

# Create your views here.
@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    
    elif request.method == "GET":
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
@require_http_methods(["POST"])
def logout(request):
    auth_logout(request)
    return redirect('boards:index')


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')            
    
    elif request.method == "GET":
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
@require_http_methods(["POST"])
def follow(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect('accounts:profile', user_pk)


@login_required
@require_http_methods(["GET", "POST"])
def profile(request, user_pk):
    try:
        boards = get_list_or_404(Board, author_id=user_pk)
    except:
        boards = None
    try:
        comments = get_list_or_404(Comment, author_id=user_pk)
    except:
        comments = None
    
    profile_user = User.objects.get(id=user_pk)

    context = {
        'boards': boards,
        'comments': comments,
        'profile_user': profile_user,
    }
    return render(request, 'accounts/profile.html', context)