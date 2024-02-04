# Generated by Django 5.0 on 2024-02-04 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_published_date'),
        ('location', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='library_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='location.library_location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]