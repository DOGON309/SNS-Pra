from django.urls import path
from .views import GoodView, BadView

urlpatterns = [
    path('<int:id>', GoodView, name = 'good'),
    path('view/<int:id>', BadView),
]