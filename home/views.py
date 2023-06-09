from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.forms import CommentForm
from post.models import PostModel, CommentModel

@login_required(login_url = '/accounts/login')
def HomeView(request):
    params = {
        'title': 'HOME',
        'items': '',
    }
    params['items'] = PostModel.objects.all()
    return render(request, 'home/home.html', params)

@login_required(login_url = '/accounts/login/')
def CommentView(request, id):
    params = {
        'title': 'コメント',
        'form': CommentForm,
        'post': '',
        'items': '',
    }
    post = PostModel.objects.get(id = id)
    params['post'] = post
    params['items'] = CommentModel.objects.filter(post = post).order_by('-up_date', )
    return render(request, 'home/comment.html', params)