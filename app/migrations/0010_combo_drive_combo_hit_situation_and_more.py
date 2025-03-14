# Generated by Django 5.0.3 on 2025-02-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_combo_frames_alter_character_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo',
            name='Drive',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='combo',
            name='hit_situation',
            field=models.CharField(choices=[('normal', '通常以上'), ('counter', 'カウンター以上限定'), ('punish', 'パニカン限定')], default='通常以上', max_length=10),
        ),
        migrations.AlterField(
            model_name='combo',
            name='input_type',
            field=models.CharField(choices=[('m', 'M'), ('c', 'C'), ('m & c', 'M & C')], default='m & c', max_length=10),
        ),
    ]
