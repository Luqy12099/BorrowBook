# Generated by Django 5.0 on 2024-01-30 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementUser', '0002_admin_library_decsription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_library',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]