from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 255,default="")
    slug = models.SlugField(default="")
    intro = models.TextField(default="")
    body = models.TextField(default="")
    posted_date = models.DateTimeField(auto_now_add = True)

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
    ('mai', 'Mai'),
    ('manon', 'Manon'),
    ('marisa', 'Marisa'),
    ('rashid', 'Rashid'),
    ('ryu', 'Ryu'),
    ('terry', 'Terry'),
    ('vega', 'Vega'),
    ('zangief', 'Zangief')
]

class Character(models.Model):
    name = models.CharField(max_length=50, choices=CHARACTER_CHOICES)  # 選択式のフィールド
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='characters/', blank=True)

    def __str__(self):
        return self.get_name_display()  # フルネームを返す

class Combo(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)  # キャラクターとの紐づけ
    title = models.CharField(max_length=100)  # コンボのタイトル
    description = models.TextField()  # コンボの内容
    input_type = models.CharField(max_length=50, choices=[('m', 'M'), ('c', 'C'), ('m & c', 'M & C')],default='m & c')  # 操作タイプ
    difficulty = models.CharField(max_length=6, choices=[('easy', '初級'), ('medium', '中級'),('hard','上級')],default='初級')  # 難易度
    damage = models.PositiveIntegerField(default=0)  # ダメージ数
    okizeme = models.BooleanField(default=False)  # 起き攻めの有無
    situation = models.TextField(blank=True, null=True)  # 起き攻めの状況説明
    frames = models.PositiveIntegerField(blank=True, null=True)  # フレーム数（オプション）
    video = models.FileField(upload_to='videos/', blank=True, null=True)  # 動画ファイル用のフィールド

    def __str__(self):
        return f"{self.title} - {self.character.name}"