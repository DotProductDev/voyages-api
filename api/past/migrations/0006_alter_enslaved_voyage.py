# Generated by Django 4.2.1 on 2023-06-30 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0005_voyage_human_reviewed'),
        ('past', '0005_alter_enslaved_age_alter_enslaved_captive_fate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enslaved',
            name='voyage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voyage_enslaved_people', to='voyage.voyage'),
        ),
    ]
