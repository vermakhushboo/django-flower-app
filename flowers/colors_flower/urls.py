from django.urls import path
from django.urls import path
from .views import flower

urlpatterns = [
    path('flower/', flower, name="flowers")
]