from django.urls import path
from .views import HomeView, CommentView

urlpatterns = [
    path('', HomeView, name = 'home'),
    path('comment/<int:id>', CommentView, name = 'comment'),
]