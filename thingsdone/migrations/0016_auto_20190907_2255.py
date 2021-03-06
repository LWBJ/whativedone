# Generated by Django 2.2.5 on 2019-09-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thingsdone', '0015_auto_20190907_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thingdone',
            name='difficulty',
            field=models.CharField(choices=[('Trivial', 'Trivial'), ('Normal', 'Normal'), ('Challenging', 'Challenging'), ('Arduous', 'Arduous'), ('Rabz Kebabz', 'Rabz Kebabz')], default='Normal', help_text='How challenging was the task?', max_length=200),
        ),
    ]
