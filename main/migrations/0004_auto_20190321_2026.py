# Generated by Django 2.1.5 on 2019-03-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_picture_mountains'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='photo',
            new_name='photo1',
        ),
        migrations.AddField(
            model_name='picture',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='wgrane_zdjecia'),
        ),
        migrations.AddField(
            model_name='picture',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='wgrane_zdjecia'),
        ),
        migrations.AddField(
            model_name='picture',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='wgrane_zdjecia'),
        ),
    ]