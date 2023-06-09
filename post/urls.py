from django.urls import path
from .views import PostView, CommentView

urlpatterns = [
    path('', PostView, name = 'post'),
    path('comment/<int:id>', CommentView)
]