from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 255,default="")
    slug = models.SlugField(default="")
    intro = models.TextField(default="")
    body = models.TextField(default="")
    posted_date = models.DateTimeField(auto_now_add = True)

class Combo(models.Model):
    CHARACTER_CHOICES = [
        ('aki', 'Aki'),
        ('blanka', 'Blanka'),
        ('cammy', 'Cammy'),
        ('chunli', 'Chunli'),
        ('dhalsim', 'Dhalsim'),
        ('dj', 'Dj'),
        ('ed', 'Ed'),
        ('gouki', 'Gouki'),
        ('guile', 'Guile'),
        ('honda', 'Honda'),
        ('jamie', 'Jamie'),
        ('jp', 'Jp'),
        ('juri', 'Juri'),
        ('ken', 'Ken'),
        ('kimbery', 'Kimbery'),
        ('lily', 'Lily'),
        ('luke', 'Luke'),
        ('manon', 'Manon'),
        ('marisa', 'Marisa'),
        ('rashid', 'Rashid'),
        ('ryu', 'Ryu'),
        ('terry', 'Terry'),
        ('vega', 'Vega'),
        ('zangief', 'Zangief')
    ]

    character = models.CharField(max_length=50, choices=CHARACTER_CHOICES)
    name = models.CharField(max_length=100)
    input_sequence = models.TextField()
    description = models.TextField(blank=True)