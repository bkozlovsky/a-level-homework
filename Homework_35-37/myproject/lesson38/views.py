from django.shortcuts import render
from .models import Visit, Visitor, Animal, Ticket
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import AnimalCreateForm
from django.contrib.auth.views import LoginView

# Create your views here.

animals_list = Animal.objects.all().order_by('arrival_date')

def startpage(request):
    return render(request, 'startpage.html', {'animals': animals_list})


def temp1(request):
    return render(request, 'temp1.html')


def temp2(request):
    return render(request, 'temp2.html')


def temp3(request):
    return render(request, 'temp3.html')


def verynew(request):
    return render(request, 'verynew.html')


def animal(request, animal_id):
    data = {}
    for animal in animals_list:
        if animal.id == animal_id:
            data = {
                'nickname': animal.nickname,
                'species': animal.species,
                'age': animal.age,
                'gender': animal.gender,
                'all_visits': Visit.objects.filter(animal_id=animal.id),
                'arrival_date': animal.arrival_date
            }
    return render(request, 'animal_info.html', data)


class CreateAnimal(CreateView):

    model = Animal
    form_class = AnimalCreateForm
    template_name = 'create_animal.html'
    success_url = '/'

class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = 'animal_delete.html'
    success_url = '/'