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