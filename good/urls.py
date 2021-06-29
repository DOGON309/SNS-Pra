from django.urls import path
from .views import GoodView

urlpatterns = [
    path('<int:id>', GoodView, name = 'good'),
]