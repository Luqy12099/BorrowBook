# Generated by Django 5.0 on 2024-01-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('admin', 'Admin'), ('superadmin', 'Super Admin')], default='user', max_length=20),
        ),
    ]
