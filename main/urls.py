from django.urls import path
from .views import wszystkie_zdjecia, nowe_zdjecie

urlpatterns = [
    path('zdjecia/', wszystkie_zdjecia, name='wszystkie_zdjecia'),
    path('nowy/', nowe_zdjecie, name='nowe_zdjecie'),
]