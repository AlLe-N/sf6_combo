# Generated by Django 5.0.3 on 2025-02-20 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_combo_drive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='intro',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
