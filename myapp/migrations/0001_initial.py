# Generated by Django 4.2.5 on 2024-11-24 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gejala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Penyakit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('definisi', models.TextField()),
                ('solusi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BasisPengetahuan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bobot', models.FloatField()),
                ('kode_gejala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.gejala')),
                ('kode_penyakit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.penyakit')),
            ],
        ),
    ]
