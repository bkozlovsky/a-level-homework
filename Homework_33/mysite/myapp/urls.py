from django.urls import path

from .views import page_id

urlpatterns = [
    path('product', page_id),
    path('product/<int:number>', page_id),
    path('product/<int:number>/create', page_id),
    path('product/<int:number>/delete', page_id),
    path('product/<int:number>/info', page_id),
    path('product/<int:number>/<slug:name>', page_id),
]