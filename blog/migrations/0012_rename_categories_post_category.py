# Generated by Django 4.0.1 on 2022-01-25 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='category',
        ),
    ]
