from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name="index.html"

class Testpage(TemplateView):
    template_name='test.html'

class Thanks(TemplateView):
    template_name='thanks.html'
