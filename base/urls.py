from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='homr'),
    path('home/', views.home, name='main'),
    path('dairy/', views.dairy, name='dairy'),
]


