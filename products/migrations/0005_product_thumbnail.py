# Generated by Django 5.0.4 on 2024-05-01 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_ourinstagramstory_story_link'),
        ('products', '0004_category_level_category_lft_category_rght_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media'),
        ),
    ]
