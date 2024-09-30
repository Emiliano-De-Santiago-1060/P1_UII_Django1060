from django.urls import path
from . import views
urlpatterns = [
    path("", views.hola, name="DeSantiagoclase_app")
]
