from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 255,default="")
    body = models.TextField(default="")
    posted_date = models.DateTimeField(auto_now_add = True)

CHARACTER_CHOICES = [
    ('ryu', 'Ryu'),
    ('luke', 'Luke'),
    ('jamie', 'Jamie'),
    ('chunli', 'Chunli'),
    ('guile', 'Guile'),
    ('kimbery', 'Kimbery'),
    ('juri', 'Juri'),
    ('ken', 'Ken'),
    ('blanka', 'Blanka'),
    ('dhalsim', 'Dhalsim'),
    ('honda', 'Honda'),
    ('deejay', 'Deejay'),
    ('manon', 'Manon'),
    ('marisa', 'Marisa'),
    ('jp', 'Jp'),
    ('zangief', 'Zangief'),
    ('lily', 'Lily'),
    ('cammy', 'Cammy'),
    ('rashid', 'Rashid'),
    ('aki', 'Aki'),
    ('ed', 'Ed'),
    ('gouki', 'Gouki'),
    ('vega', 'Vega'),
    ('terry', 'Terry'),
    ('mai', 'Mai'),
    ('elena','Elena'),
    ('sagat','Sagat')
]

class Character:
    """キャラクターを定義"""
    def __init__(self, key):
        self.key = key
        self.name = dict(CHARACTER_CHOICES).get(key, key.capitalize())

    def get_image_url(self):
            """キャラクターの画像URLを返す"""
            return f"/static/app/images/{self.name.lower()}.png"

class Combo(models.Model):
    character = models.CharField(max_length=20, choices=CHARACTER_CHOICES)  # キャラクターとの紐づけ
    title = models.CharField(max_length=100)  # コンボのタイトル
    description = models.TextField()  # コンボの内容
    input_type = models.CharField(max_length=10, choices=[('m', 'M'), ('c', 'C'), ('m & c', 'M & C')],default='m & c')  # 操作タイプ
    difficulty = models.CharField(max_length=6, choices=[('easy', '初級'), ('medium', '中級'),('hard','上級')],default='初級')  # 難易度
    hit_situation = models.CharField(max_length=20, choices=[('normal', '通常'),('counter', 'カウンター'),('punish','パニカン')],default='通常')  # ヒット状況
    Drive = models.IntegerField(choices=[(i, str(i)) for i in range(7)], default='0')  # ドライブゲージの使用本数
    damage = models.PositiveIntegerField(default=0)  # ダメージ数
    okizeme = models.BooleanField(default=False)  # 起き攻めの有無
    situation = models.TextField(blank=True, null=True)  # 起き攻めの状況説明
    frames = models.PositiveIntegerField(blank=True, null=True)  # フレーム数（オプション）
    video = models.FileField(upload_to='videos/', blank=True, null=True)  # 動画ファイル用のフィールド

    def __str__(self):
        return f"{self.title} - {self.character}"