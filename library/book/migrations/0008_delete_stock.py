# Generated by Django 5.0 on 2024-02-04 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_merge_0005_stock_0006_alter_author_middle_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='stock',
        ),
    ]
