from .models import Picture
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PictureForm


def wszystkie_zdjecia(request):
    zdjecia = Picture.objects.all()
    return render(request, 'trip_list.html', {'zdjecia': zdjecia})


@login_required
def nowe_zdjecie(request):
    form = PictureForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_zdjecia)

    return render(request, 'picture_form.html', {'form': form})