from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import re

# Create your views here.
def static_url(request):
    message = ""
    if "new" in request.get_full_path():
        message = "Your're creating new comment"
    if "edit" in request.get_full_path():
        message = "Your're editing a comment"
    if "lock" in request.get_full_path():
        message = "You've locked a comment"

    return render(request, 'index.html', {'static_url_message': message})

def dynamic_url(request, id=None):
    message = ""
    if "add" in request.get_full_path():
        message = "You've added comment with id: {}".format(id)
    if "delete" in request.get_full_path():
        message = "You've deleted comment with id: {}".format(id)
    if request.get_full_path() == f"/comment/{id}":
        message = "This is comment with id: {}".format(id)
    return render(request, 'index.html', {'dynamic_url_message': message})

def diff_url(request, string=None):
    message = ""
    ukr_operator = {
        'kyivstar' : "^\+?3?8?(0(67|68|96|97|98)\-\d{3}\-\d{2}\-\d{2})$",
        'vodafone': "^\+?3?8?(0(66|95|99)\-\d{3}\-\d{2}\-\d{2})$",
        'lifecell': "^\+?3?8?(0[679]3\-\d{3}\-\d{2}\-\d{2})$",
    }
    if re.match(ukr_operator['kyivstar'], string):
        message = "This is comment with Kyivstar number: {}".format(string)
    elif re.match(ukr_operator['vodafone'], string):
        message = "This is comment with Vodafone number: {}".format(string)
    elif re.match(ukr_operator['lifecell'], string):
        message = "This is comment with Lifecell number: {}".format(string)
    else:
        message = "This is comment with custom url: {}".format(string)

    return render(request, 'index.html', {'regex': message})