from django.urls import path
from .views import all_trips, new_trip, edit_trip, delete_trip

urlpatterns = [
    path('trips/', all_trips, name='wszystkie_wyjazdy'),
    path('new/', new_trip, name='nowy_wyjazd'),
    path('edit/<int:id>/', edit_trip, name='edytuj_wyjazd'),
    path('delete/<int:id>/', delete_trip, name='usun_wyjazd'),
]