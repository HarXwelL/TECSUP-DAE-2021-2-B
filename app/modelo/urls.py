from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8080/app/
    path('', views.index, name='index'),
    # ex: localhost:8080/app/suma/
    path('suma/', views.suma, name='detail'),
    # ex: localhost:8080/app/suma/18
    path('suma/<int:num1>/', views.num1, name='results'),
    # ex: localhost:8080/app/suma/18/19
    path('suma/<int:num1>/<int:num2>/', views.num2, name='results1'),
    # ex: localhost:8080/suma/18/19/result/
    path('suma/<int:num1>/<int:num2>/result', views.votar, name='vote'),

]
