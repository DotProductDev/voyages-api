# Generated by Django 4.2.1 on 2023-06-30 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0004_voyagesources_transkribus_docid'),
    ]

    operations = [
        migrations.AddField(
            model_name='voyage',
            name='human_reviewed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
