from django.shortcuts import render, redirect
from post.models import PostModel
from .models import GoodModel

def GoodView(request, id):
    params = {
        'title': 'GOOD',
    }
    model = GoodModel()
    user = request.user
    model.owner = user
    model.message_id = PostModel.objects.get(pk = id)
    model.save()
    cnt = PostModel.objects.get(pk = id)
    cnt.good_count += 1
    cnt.save()
    return redirect('/home')

def BadView(request, id):
    params = {
        'title': 'グッドした人',
        'items': '',
    }
    model = PostModel.objects.get(pk = id)
    params['items'] = GoodModel.objects.filter(message_id = model)
    return render(request, 'good/bad.html', params)