# Generated by Django 2.1.5 on 2019-03-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
