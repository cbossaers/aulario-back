from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('usuario/', views.UserList.as_view()),
    path('usuario/<int:pk>/', views.UserDetail.as_view()),
    path('aula/', views.AulaList.as_view()),
    path('aula/<int:pk>/', views.AulaDetail.as_view()),
    path('asignatura/', views.AsignaturaList.as_view()),
    path('asignatura/<int:pk>/', views.AsignaturaDetail.as_view()),
    path('curso/', views.CursoList.as_view()),
    path('curso/<int:pk>/', views.CursoDetail.as_view()),
    path('reserva/', views.ReservaList.as_view()),
    path('reserva/<int:pk>/', views.ReservaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)