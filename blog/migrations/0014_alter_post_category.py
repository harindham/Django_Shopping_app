# Generated by Django 4.0.1 on 2022-01-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('electronics', 'electronics'), ('shoes', 'shoes'), ('tshirt', 'tshirt')], default='available', max_length=60),
        ),
    ]
