# Generated by Django 2.1.5 on 2019-03-19 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190318_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='mountains',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
    ]
