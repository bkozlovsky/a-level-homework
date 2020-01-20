from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

SPECIES_CHOICES = [
    ('Monkey', 'Monkey'),
    ('Badger', 'Badger'),
    ('Bear', 'Bear'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class Animal(models.Model):
    species = models.CharField(max_length=60, choices=SPECIES_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    nickname = models.CharField(max_length=120)
    arrival_date = models.DateField(null=False)

    def __str__(self):
        return f"{self.species} - {self.nickname}"

class Visitor(User):
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Ticket(models.Model):
    age_limit = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)])
    expiration_date = models.DateField()
    visitor = models.OneToOneField(Visitor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket {self.id} for {self.visitor.first_name}"

    def save(self, **kwargs):
        if not self.id:
            dt = timezone.now() + timezone.timedelta(days=1)
            self.expiration_date = dt
        super().save(**kwargs)

class Visit(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.visitor.first_name} {self.visitor.last_name} visited {self.animal.nickname}"



