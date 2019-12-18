from django.urls import path, re_path

from .views import static_url, dynamic_url, diff_url

urlpatterns = [
    path('article/new', static_url),
    path('article/edit', static_url),
    path('article/lock', static_url),
    path('article/<int:id>', dynamic_url),
    path('article/<int:id>/add', dynamic_url),
    path('article/<int:id>/delete', dynamic_url),
    re_path('article/' + r'([A-Za-z0-9\-\_]+)', diff_url),
    re_path('article/' + r'^\+?3?8?(0(67|68|96|97|98)\-\d{3}\-\d{2}\-\d{2})$', diff_url),
    re_path('article/' + r'^\+?3?8?(0(66|95|99)\-\d{3}\-\d{2}\-\d{2})$', diff_url),
    re_path('article/' + r'^\+?3?8?(0[679]3\-\d{3}\-\d{2}\-\d{2})$', diff_url),
]