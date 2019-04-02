from django.urls import path
from .views import all_trips, new_trip, edit_trip, delete_trip

from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, PictureViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pictures', PictureViewSet)


urlpatterns = [
    path('trips/', all_trips, name='wszystkie_wyjazdy'),
    path('new/', new_trip, name='nowy_wyjazd'),
    path('edit/<int:id>/', edit_trip, name='edytuj_wyjazd'),
    path('delete/<int:id>/', delete_trip, name='usun_wyjazd'),
    path('', include(router.urls)),
]