# Generated by Django 4.0.2 on 2022-07-27 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0011_voyage_african_info_voyage_cargo'),
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doc', to='voyage.voyagesources', verbose_name='Source'),
        ),
    ]
