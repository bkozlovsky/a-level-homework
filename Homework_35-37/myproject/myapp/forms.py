from django import forms

ENG_LEVELS_CHOICE = [
    ('A0', 'Starter'),
    ('A1', 'Elementary'),
    ('A2', 'Pre Intermediate'),
    ('B1', 'Intermediate'),
    ('B2', 'Upper Intermediate'),
    ('C1', 'Advanced'),
    ]
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F','Female'),
]

class MyForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100, required=False)
    eng_levels = forms.ChoiceField(required=False, choices=ENG_LEVELS_CHOICE)
    gender = forms.ChoiceField(required=False, choices=GENDER_CHOICES)
    age = forms.IntegerField(required=False)