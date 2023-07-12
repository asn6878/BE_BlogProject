from django.urls import path, include

from .views import *

urlpatterns = [
    path('',UserView.as_view(), name='userView'),
    path('<int:pk>/',UserDetailView.as_view()),
    path('managements/<int:pk>/', UserDetailManagementView.as_view()),
]