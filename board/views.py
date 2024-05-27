from django.shortcuts import render, get_object_or_404
from .models import Board

def board_list(request):
    boards = Board.objects.all()
    return render(request, 'board/board_list.html', {'boards': boards})

def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'board/board_detail.html', {'board': board})