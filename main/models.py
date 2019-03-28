from django.db import models


class Picture(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(default='')
    year = models.IntegerField(null=True, blank=True)
    mountains = models.CharField(max_length=126, null=True, blank=True)
    photo1 = models.ImageField(null=True, blank=True, upload_to='wgrane_zdjecia')
    photo2 = models.ImageField(null=True, blank=True, upload_to='wgrane_zdjecia')
    photo3 = models.ImageField(null=True, blank=True, upload_to='wgrane_zdjecia')
    photo4 = models.ImageField(null=True, blank=True, upload_to='wgrane_zdjecia')
    photo5 = models.ImageField(null=True, blank=True, upload_to='wgrane_zdjecia')
    photo6 = models.ImageField(null=True, blank=True, upload_to='wgrane_zdjecia')

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.name)
