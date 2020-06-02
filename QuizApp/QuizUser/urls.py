
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('quiz', views.quiz, name='quiz'),
    path('next_que/<int:qno>', views.next_que, name='next_que'),
]
