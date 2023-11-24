from django.urls import path
from .views import *


urlpatterns = [
    path('register/', CustomUserApiView.as_view()),
    path('login/', LoginView.as_view()),
]
