# Generated by Django 4.0.1 on 2022-01-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_post_content_post_price_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default="A product description is the marketing copy that explains what a product is and why it's worth purchasing. The purpose of a product description is to supply customers with important information", max_length=100),
            preserve_default=False,
        ),
    ]