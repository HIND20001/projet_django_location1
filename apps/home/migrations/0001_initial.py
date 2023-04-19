# Generated by Django 3.2.6 on 2023-04-17 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=100)),
                ('matricule', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('prix', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='vehicule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('puissance', models.IntegerField()),
                ('nbr_place', models.IntegerField()),
                ('auto_menu', models.CharField(max_length=100)),
                ('prix', models.FloatField()),
                ('photo', models.CharField(max_length=100)),
            ],
        ),
    ]