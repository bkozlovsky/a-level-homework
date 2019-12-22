from django.urls import path

from .views import index, index2, index3

urlpatterns = [
    path('', index, name='index'),
    path('<int:number>/', index2, name='index2'),
    path('<str:text>/', index3, name='index3'),
]