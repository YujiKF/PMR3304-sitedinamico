# Generated by Django 5.1.3 on 2024-11-17 18:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_created_at_post_created_date_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]