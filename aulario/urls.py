from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('usuario/', views.UserList.as_view()),
    path('usuario/<int:pk>/', views.UserDetail.as_view()),
    path('aula/', views.AulaList.as_view()),
    path('aula/<int:pk>/', views.AulaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)