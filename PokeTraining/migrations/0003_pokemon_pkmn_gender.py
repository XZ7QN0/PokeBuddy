# Generated by Django 2.2.1 on 2019-06-24 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PokeTraining', '0002_auto_20190623_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='pkmn_gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('G', 'Genderless')], default='G', max_length=11),
        ),
    ]
