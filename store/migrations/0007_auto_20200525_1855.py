# Generated by Django 3.0.6 on 2020-05-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200525_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null='True'),
        ),
    ]
