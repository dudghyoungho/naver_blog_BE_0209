# Generated by Django 5.1 on 2025-01-31 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comment_like_count_commentheart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('everyone', '전체 공개'), ('mutual', '서로 이웃만 공개'), ('me', '나만 보기')], default='everyone', max_length=10, verbose_name='공개 범위'),
        ),
    ]
