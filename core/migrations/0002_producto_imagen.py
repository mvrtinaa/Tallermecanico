# Generated by Django 4.2.2 on 2023-07-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='nn.jpg', upload_to='imagenes/', verbose_name='imagen'),
        ),
    ]
