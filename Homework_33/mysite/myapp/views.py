from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def page_id(request, number=None, name=None):
    blank_page = "This is blank product page"
    create_response = "You've created product with ID: {}".format(number)
    delete_response = "You've deleted product with ID: {}".format(number)
    info_response = "This is info page of the product with ID: {}".format(number)
    slug_response = "This is the product with ID: {} and slug: {}".format(number, name)
    id_page = "This is product with ID: {}".format(number)
    if "create" in request.get_full_path():
        return render(request, 'index.html', {'create_response': create_response})
    if "delete" in request.get_full_path():
        return render(request, 'index.html', {'delete_response': delete_response})
    if "info" in request.get_full_path():
        return render(request, 'index.html', {'info_response': info_response})
    if name:
        return render(request, 'index.html', {'slug_response': slug_response})
    if type(request.get_full_path().strip('/product/')) == str:
        return render(request, 'index.html', {'id_page': id_page})
    else:
        return render(request, 'index.html', {'blank_page': blank_page})