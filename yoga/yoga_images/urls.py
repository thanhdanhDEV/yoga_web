from django.urls import path

from . import views

app_name = 'yoga_images'
urlpatterns = [
    path('', view=views.index, name="index"),
]