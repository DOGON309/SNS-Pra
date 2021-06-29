from django.urls import path
from .views import LoginView, SignupView, LogoutView

urlpatterns = [
    path('login/', LoginView, name = 'login'),
    path('signup/', SignupView, name = 'signup'),
    path('logout/', LogoutView, name = 'logout'),
]