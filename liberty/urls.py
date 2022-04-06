from django.urls import path
from liberty import views

urlpatterns = [
    path("", views.index, name="index"),
]
