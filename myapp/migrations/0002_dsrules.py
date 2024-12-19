# Generated by Django 4.2.5 on 2024-11-28 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DsRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bobot', models.FloatField()),
                ('id_gejala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.gejala')),
                ('id_penyakit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.penyakit')),
            ],
        ),
    ]
