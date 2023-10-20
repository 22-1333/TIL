from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from accounts.models import User

# Create your views here.
@require_http_methods(["GET"])
def index(request):
    boards = Board.objects.all().order_by('-created_at')
    context = {
        'boards': boards
    }
    return render(request, 'boards/index.html', context)


@require_http_methods(["GET", "POST"])
def detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        if board.author == request.user:
            board.delete()
            return redirect('boards:index')

    comments = board.comments.all()
    comment_form = CommentForm()
    user_name = User.objects.get(id=board.author_id)

    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
        'user_name': user_name,
    }
    return render(request, 'boards/detail.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if board.author == request.user:
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                form.save()
                return redirect('boards:detail', board.pk)
        else:
            form = BoardForm(instance=board)
        context = {
            'board': board,
            'form': form,
        }        
        return render(request, 'boards/update.html', context)
    else:
        return redirect("boards:detail", pk)


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            form.save()
            return redirect('boards:index')
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'boards/create.html', context)


@login_required
@require_http_methods(["POST"])
def comment(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.board = board
            comment.save()
            return redirect('boards:detail', board.pk)


@login_required
@require_http_methods(["POST"])
def comment_detail(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.author == request.user:        
        if request.method == 'POST':
            comment.delete()
            return redirect('boards:detail', board_pk)
    else:
        return redirect('boards:detail', board_pk)
    

@login_required
@require_http_methods(["POST"])
def likes(request, pk):
    board = Board.objects.get(pk=pk)
    if request.user in board.like_users.all():
        board.like_users.remove(request.user)
    else:
        board.like_users.add(request.user)
    return redirect('boards:detail', pk)