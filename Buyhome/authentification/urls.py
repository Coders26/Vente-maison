from django.urls import path

from . import views

urlpatterns = [
    path('', views.authentification, name="authentification"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.deconnexion, name="logout"),
]