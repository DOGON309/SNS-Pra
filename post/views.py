from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import PostModel, CommentModel

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

def CommentView(request, id):
    if request.method == 'POST':
        model = CommentModel()
        model.post = PostModel.objects.get(id = id)
        model.owner = request.user
        model.content = request.POST['content']
        model.save()
        return redirect('/home/comment/' + str(id))
    else:
        return redirect('/home')