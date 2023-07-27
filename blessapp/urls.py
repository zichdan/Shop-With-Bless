from django.urls import path, include
from blessapp import views




urlpatterns = [
    path('', views.index, name='index')
]
