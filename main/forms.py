from django.forms import ModelForm
from .models import Picture


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['name', 'description', 'year', 'month', 'mountains', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5',
                  'photo6']
