# Generated by Django 2.2.7 on 2019-11-23 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examtool', '0003_remove_category_sub_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer1',
            field=models.CharField(default='', max_length=128, verbose_name='選択肢1'),
        ),
        migrations.AddField(
            model_name='question',
            name='answer2',
            field=models.CharField(default='', max_length=128, verbose_name='選択肢2'),
        ),
        migrations.AddField(
            model_name='question',
            name='answer3',
            field=models.CharField(default='', max_length=128, verbose_name='選択肢3'),
        ),
        migrations.AddField(
            model_name='question',
            name='answer4',
            field=models.CharField(default='', max_length=128, verbose_name='選択肢4'),
        ),
        migrations.AddField(
            model_name='question',
            name='category_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='question_category', to='examtool.Category', verbose_name='カテゴリ'),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='question',
            name='seikai',
            field=models.IntegerField(default=0, verbose_name='正解番号'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='', max_length=128, verbose_name='カテゴリ'),
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
    ]
