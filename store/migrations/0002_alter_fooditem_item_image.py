# Generated by Django 4.2.4 on 2023-08-24 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='item_image',
            field=models.FileField(blank=True, null=True, upload_to='items/'),
        ),
    ]
