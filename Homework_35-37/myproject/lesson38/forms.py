from django.forms import ModelForm
from .models import Animal, Visitor
from django.utils import timezone


class AnimalCreateForm(ModelForm):

    class Meta:

        model = Animal
        fields = ['species', 'gender', 'age', 'nickname']

    def save(self):
        animal = super(AnimalCreateForm, self).save(commit=False)
        animal.arrival_date = timezone.now()
        animal.save()
        return animal