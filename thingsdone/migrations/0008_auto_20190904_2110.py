# Generated by Django 2.2.5 on 2019-09-04 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thingsdone', '0007_auto_20190904_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='month',
        ),
        migrations.RemoveField(
            model_name='day',
            name='week',
        ),
    ]
