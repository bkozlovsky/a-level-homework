from django.urls import path, re_path

from .views import static_url, dynamic_url, diff_url

urlpatterns = [
    path('comment/new', static_url),
    path('comment/edit', static_url),
    path('comment/lock', static_url),
    path('comment/<int:id>', dynamic_url),
    path('comment/<int:id>/add', dynamic_url),
    path('comment/<int:id>/delete', dynamic_url),
    re_path('comment/' + r'([A-Za-z0-9\-\_]+)', diff_url),
    re_path('comment/' + r'^\+?3?8?(0(67|68|96|97|98)\-\d{3}\-\d{2}\-\d{2})$', diff_url),
    re_path('comment/' + r'^\+?3?8?(0(66|95|99)\-\d{3}\-\d{2}\-\d{2})$', diff_url),
    re_path('comment/' + r'^\+?3?8?(0[679]3\-\d{3}\-\d{2}\-\d{2})$', diff_url),
]