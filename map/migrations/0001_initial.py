# Generated by Django 2.0.5 on 2018-05-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taizhou',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField(blank=True)),
                ('mi2', models.BigIntegerField()),
                ('tel', models.TextField(blank=True)),
                ('avg', models.BigIntegerField()),
                ('howsell', models.TextField(blank=True)),
                ('getdate', models.DateTimeField()),
                ('GPS_lat', models.TextField(blank=True)),
            ],
        ),
    ]
