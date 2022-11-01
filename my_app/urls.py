from django.urls import path

from my_app import views

app_name = "my_app"
urlpatterns = [ 
    path("meca", views.meca, name = "meca-list"),
    path("segundo", views.meca, name = "segundo-list")
]