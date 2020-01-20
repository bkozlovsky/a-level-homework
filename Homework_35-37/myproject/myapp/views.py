from .forms import MyForm
from django.views.generic import FormView

class MyFormView(FormView):
    template_name = 'index.html'
    http_method_names = ['get', 'post']
    form_class = MyForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        print('GET REQUEST')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('POST REQUEST')
        return super().post(request, *args, **kwargs)