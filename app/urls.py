from django.urls import path

from .views import inicio, curso, estudiantes, profesores, acerca

urlpatterns = [
    path('', inicio, name='inicio'),
    path('curso', curso, name='curso'),
    path('profesores', profesores, name='profesores'),
    path('estudiantes', estudiantes, name='estudiantes'),
    path('acerca', acerca, name='acerca'),
]