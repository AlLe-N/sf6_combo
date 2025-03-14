# Generated by Django 5.0.3 on 2024-10-29 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('aki', 'Aki'), ('blanka', 'Blanka'), ('cammy', 'Cammy'), ('chunli', 'Chunli'), ('dhalsim', 'Dhalsim'), ('dj', 'Dj'), ('ed', 'Ed'), ('gouki', 'Gouki'), ('guile', 'Guile'), ('honda', 'Honda'), ('jamie', 'Jamie'), ('jp', 'Jp'), ('juri', 'Juri'), ('ken', 'Ken'), ('kimbery', 'Kimbery'), ('lily', 'Lily'), ('luke', 'Luke'), ('manon', 'Manon'), ('marisa', 'Marisa'), ('rashid', 'Rashid'), ('ryu', 'Ryu'), ('terry', 'Terry'), ('vega', 'Vega'), ('zangief', 'Zangief')], max_length=50)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='characters/')),
            ],
        ),
        migrations.RenameField(
            model_name='combo',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='combo',
            name='input_sequence',
        ),
        migrations.AddField(
            model_name='combo',
            name='damage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='combo',
            name='difficulty',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='combo',
            name='input_type',
            field=models.CharField(choices=[('modern', 'Modern'), ('classic', 'Classic')], default='classic', max_length=50),
        ),
        migrations.AddField(
            model_name='combo',
            name='okizeme',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='combo',
            name='video',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='combo',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='combo',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.character'),
        ),
    ]
