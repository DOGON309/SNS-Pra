from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import PostModel

@login_required(login_url = '/accounts/login')
def HomeView(request):
    params = {
        'title': 'HOME',
        'items': '',
    }
    model = PostModel
    params['items'] = model.objects.all()
    return render(request, 'home/home.html', params)