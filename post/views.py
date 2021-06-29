from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import PostModel

@login_required(login_url = '/accounts/login/')
def PostView(request):
    params = {
        'title': 'POST',
        'form': PostForm,
    }
    if request.method == 'POST':
        content = request.POST['content']
        model = PostModel()
        model.owner = request.user
        model.content = content
        model.save()
        return redirect('/home')
    return render(request, 'post/post.html', params)