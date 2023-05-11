# Generated by Django 4.2 on 2023-05-03 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventurezone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('open', models.BooleanField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='attractions',
            options={},
        ),
        migrations.AlterModelOptions(
            name='park',
            options={},
        ),
        migrations.AlterModelOptions(
            name='restaurants',
            options={},
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='adventurezone.place')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='adventurezone.place')),
            ],
        ),
    ]
