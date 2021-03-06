# Generated by Django 2.2.5 on 2019-09-07 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thingsdone', '0014_auto_20190906_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='month',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='thingsdone.Month'),
        ),
        migrations.AlterField(
            model_name='day',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='day',
            name='week',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='thingsdone.Week'),
        ),
        migrations.AlterField(
            model_name='month',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thingdone',
            name='day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='thingsdone.Day'),
        ),
        migrations.AlterField(
            model_name='thingdone',
            name='month',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='thingsdone.Month'),
        ),
        migrations.AlterField(
            model_name='thingdone',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thingdone',
            name='week',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='thingsdone.Week'),
        ),
        migrations.AlterField(
            model_name='week',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
