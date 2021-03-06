# Generated by Django 2.2.5 on 2019-09-06 09:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thingsdone', '0011_auto_20190906_1730'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='day',
            unique_together={('day', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='month',
            unique_together={('start_day', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='week',
            unique_together={('start_day', 'user')},
        ),
    ]
