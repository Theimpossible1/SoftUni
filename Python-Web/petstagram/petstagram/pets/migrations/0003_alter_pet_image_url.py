# Generated by Django 3.2.3 on 2021-07-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.ImageField(max_length=200, upload_to='images'),
        ),
    ]
