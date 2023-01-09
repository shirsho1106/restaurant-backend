# Generated by Django 4.1.5 on 2023-01-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default=None, upload_to='media'),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.TextField(default='money'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default='delicious food'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.TextField(default='food'),
        ),
    ]