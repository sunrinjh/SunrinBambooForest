# Generated by Django 3.1.3 on 2020-11-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]