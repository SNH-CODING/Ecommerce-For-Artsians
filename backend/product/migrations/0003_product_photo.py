# Generated by Django 4.0.4 on 2022-08-25 16:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='product_images/'),
            preserve_default=False,
        ),
    ]
