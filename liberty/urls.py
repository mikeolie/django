from django.urls import path
from liberty import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products", views.products, name="all"),
    path("logs", views.requestlog, name="all"),
    path("signin", views.signIn, name="signin"),
    path("signout", views.signOut, name="signout")
]
