# Generated by Django 4.2.5 on 2024-12-17 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_result_riwayat_result_cf_riwayat_result_ds_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='riwayat',
            name='nama',
            field=models.CharField(default='admin', max_length=200),
            preserve_default=False,
        ),
    ]
