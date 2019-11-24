from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    category_id = models.IntegerField('カテゴリID', blank=False, default=0, primary_key=True)
    category_name = models.CharField('カテゴリ', max_length=128, default='')

    def __str__(self):
        return self.category_name


class Question(models.Model):
    category_id = models.ForeignKey(Category,
                                    verbose_name='カテゴリ',
                                    related_name='question_category',
                                    default=0,
                                    on_delete=models.CASCADE)

    question = models.TextField(blank=False, default='')
    answer1 = models.CharField('選択肢1', max_length=128, default='')
    answer2 = models.CharField('選択肢2', max_length=128, default='')
    answer3 = models.CharField('選択肢3', max_length=128, default='')
    answer4 = models.CharField('選択肢4', max_length=128, default='')
    seikai = models.IntegerField('正解番号', blank=False, default=0)

    def __str__(self):
        return self.question
