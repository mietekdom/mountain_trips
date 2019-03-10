from .models import Picture
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PictureForm


def all_trips(request):
    trip = Picture.objects.all()
    return render(request, 'trip_list.html', {'trip': trip})


@login_required
def new_trip(request):
    form = PictureForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_trips)

    return render(request, 'trips_form.html', {'form': form})


@login_required
def edit_trip(request, id):
    trip = get_object_or_404(Picture, pk=id)
    form = PictureForm(request.POST or None, request.FILES or None, instance=trip)

    if form.is_valid():
        form.save()
        return redirect(all_trips)

    return render(request, 'trips_form.html', {'form': form})


@login_required
def delete_trip(request, id):
    trip = get_object_or_404(Picture, pk=id)

    if request.method == 'POST':
        trip.delete()
        return redirect(all_trips)
    return render(request, 'delete_trip.html', {'trip': trip})
