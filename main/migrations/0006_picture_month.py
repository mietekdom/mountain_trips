# Generated by Django 2.1.5 on 2019-04-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190326_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='month',
            field=models.CharField(blank=True, max_length=126, null=True),
        ),
    ]
