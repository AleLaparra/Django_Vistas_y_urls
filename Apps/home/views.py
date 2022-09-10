from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name= 'home.html'

class PaginaView(TemplateView):
    template_name= 'pagina.html'

class EstudiantesView(TemplateView):
    template_name= 'estudiantes.html'

class AdminsView(TemplateView):
    template_name= 'administradores.html'

class AcercadeView(TemplateView):
    template_name= 'acerca.html'


