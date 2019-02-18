from django.db import models


class Picture(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=600)
    photo = models.ImageField(null=True, blank=True, upload_to='wgrane_zdjecia')

    def __str__(self):
        return self.name_with_decription()

    def name_with_decription(self):
        return str(self.name) + " (" + str(self.description) + ")"
