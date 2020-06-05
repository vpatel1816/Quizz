
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('quiz', views.quiz, name='quiz'),
    path('answer/<int:qno>', views.answer, name='answer'),
    path('next/<int:qno>', views.next, name='next'),
    path('pre/<int:qno>', views.pre, name='pre'),
    path('result', views.result, name='result'),

]
