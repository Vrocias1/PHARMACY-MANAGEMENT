# Generated by Django 3.1.3 on 2020-11-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20201123_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='pict123@gmail.com', max_length=254),
        ),
    ]
