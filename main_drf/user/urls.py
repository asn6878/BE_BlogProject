from django.urls import path, include

from .views import *

urlpatterns = [
    path('',UserView.as_view(), name='register'),
    path('<int:pk>/',UserDetailView.as_view()),
]
