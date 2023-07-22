from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here idiot.

class HomePageView(TemplateView):
    template_name = 'home.html'
