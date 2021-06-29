from django.urls import path
from .views import PostView

urlpatterns = [
    path('', PostView, name = 'post'),
]