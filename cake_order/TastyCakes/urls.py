from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('normal_cake/', views.normal_cake, name='normal_cake'),
    path('eggless/', views.eggless, name='eggless'),
    path('contact/', views.contact, name='contact'),
    path('birth/', views.birth, name='birth'),
    path('anniversary/', views.anniversary, name='anniversary'),
    path('design/', views.design, name='design'),
    path('trend/', views.trend, name='trend'),
    path('photo/', views.photo, name='photo'),
    path('passion/', views.passion, name='passion'),
    path('cartoon/', views.cartoon, name='cartoon'),
    path('filmy/', views.filmy, name='filmy'),
    path('chocolate/', views.chocolate, name='chocolate'),
    path('venilla/', views.venilla, name='venilla'),
    path('black_cur/', views.black_cur, name='black_cur'),
    path('pine/', views.pine, name='pine'),
    path('red/', views.red, name='red'),
    path('blue/', views.blue, name='blue'),
    path('order/', views.order, name='order'),
    path('login/', views.login, name='login'),
    
    path('SignInSuccess/', views.SignInSuccess, name='SignInSuccess'),
    path('SignUnSuccess/', views.SignUnSuccess, name='SignUnSuccess'),
    path('', views.welcome, name='welcome'),
] 