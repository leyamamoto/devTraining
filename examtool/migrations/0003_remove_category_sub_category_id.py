# Generated by Django 2.2.7 on 2019-11-23 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examtool', '0002_auto_20191123_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category_id',
        ),
    ]
