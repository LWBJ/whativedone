# Generated by Django 2.2.5 on 2019-09-06 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('thingsdone', '0012_auto_20190906_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='month',
            name='start_day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='week',
            name='start_day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
