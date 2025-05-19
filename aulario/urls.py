from django.urls import path

from . import views

urlpatterns = [
    path("usuarios/", views.UserViewSet.list, name="usuarios"),
    #path("usuarios/<int:pk>/", views.UserViewSet.detail, name="usuario"),
]
