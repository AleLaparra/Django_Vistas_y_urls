from django.http import HttpResponse
def home (request):

#Esto es una vista 
 return HttpResponse ("Hola a todos ")#Pasamos un objeto ded tipo request como primer argumento
