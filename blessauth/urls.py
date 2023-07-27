from django.urls import path, include
from blessauth import views




urlpatterns = [
    path('signup/', views.signup, name='signup')
]
