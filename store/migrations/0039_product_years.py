# Generated by Django 3.0.6 on 2020-06-23 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_product_players_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='years',
            field=models.IntegerField(choices=[], default=2020),
        ),
    ]
