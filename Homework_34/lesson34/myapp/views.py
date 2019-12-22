""" Создать 3 страницы (https://127.0.0.1:8000/, https://127.0.0.1:8000/<int>/, https://127.0.0.1:8000/<str>/), на всех страницах должен быть хедер и футер, в хедер вставить любую картинку, в футер кнопку на https://127.0.0.1:8000/, в середине "главной" старицы сделать две кнопки, которые переходят на одну из дополнительных страниц (одна на число, вторая на строку), со случайными значениями, пример https://127.0.0.1:8000/45/ или https://127.0.0.1:8000/some_text/ """

from django.shortcuts import render
from random import randrange
import random, string

# Create your views here.
def index(request):
    random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(randrange(5, 13))])
    random_number = randrange(100, 10000)

    int_url = f"http://127.0.0.1:8000/{random_number}"
    str_url = f"http://127.0.0.1:8000/{random_string}"
    return render(request, 'index.html', {'int_url': int_url, 'str_url': str_url})

def index2(request, number):
    return render(request, 'index2.html', {'number': number})

def index3(request, text):
    return render(request, 'index3.html', {'text': text})