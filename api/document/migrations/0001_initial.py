# Generated by Django 4.2.1 on 2023-11-01 22:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voyage', '0001_initial'),
        ('past', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocSparseDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)])),
                ('month', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2000)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.URLField(blank=True, max_length=400, null=True)),
                ('iiif_manifest_url', models.URLField(blank=True, max_length=400, null=True)),
                ('iiif_baseimage_url', models.URLField(blank=True, max_length=400, null=True, unique=True)),
                ('image_filename', models.CharField(blank=True, max_length=100, null=True)),
                ('transcription', models.TextField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('human_reviewed', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShortRef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_url', models.URLField(max_length=400, null=True)),
                ('zotero_group_id', models.IntegerField(blank=True, null=True, verbose_name='Zotero Integer Group ID')),
                ('zotero_item_id', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Zotero Alphanumeric Item ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Title')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('human_reviewed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Review')),
                ('notes', models.TextField(blank=True, null=True)),
                ('date', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='document.docsparsedate', verbose_name='Date of publication or authorship')),
                ('short_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.shortref')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SourceVoyageConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_range', models.CharField(blank=True, max_length=250, null=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_voyage_connections', to='document.source')),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voyage_source_connections', to='voyage.voyage')),
            ],
        ),
        migrations.CreateModel(
            name='SourcePageConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Document page order')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_connections', to='document.page')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_connections', to='document.source')),
            ],
        ),
        migrations.CreateModel(
            name='SourceEnslaverConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_range', models.CharField(blank=True, max_length=250, null=True)),
                ('enslaver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enslaver_source_connections', to='past.enslaveridentity')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_enslaver_connections', to='document.source')),
            ],
        ),
        migrations.CreateModel(
            name='SourceEnslavementRelationConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_range', models.CharField(blank=True, max_length=250, null=True)),
                ('enslavement_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enslavement_relation_source_connections', to='past.enslavementrelation')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_enslavement_relation_connections', to='document.source')),
            ],
        ),
        migrations.CreateModel(
            name='SourceEnslavedConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_range', models.CharField(blank=True, max_length=250, null=True)),
                ('enslaved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enslaved_source_connections', to='past.enslaved')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_enslaved_connections', to='document.source')),
            ],
        ),
    ]
