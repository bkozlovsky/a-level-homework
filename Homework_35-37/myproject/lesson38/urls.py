from django.urls import path
from .views import temp1, temp2, temp3, verynew, animal, startpage, CreateAnimal, AnimalDeleteView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', startpage, name='startpage'),
    path('animal/<int:animal_id>', animal, name='animal'),
    path('temp1', temp1),
    path('temp2', temp2),
    path('final', temp3),
    path('verynew', verynew),
    path('create_animal/', CreateAnimal.as_view(), name='create_animal'),
    path('animal_delete/<int:pk>/', AnimalDeleteView.as_view(), name='animal_delete'),
    path('login/', LoginView.as_view(), name='login'),
]