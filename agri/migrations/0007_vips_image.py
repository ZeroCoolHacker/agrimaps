# Generated by Django 2.2 on 2019-07-10 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0006_vips'),
    ]

    operations = [
        migrations.AddField(
            model_name='vips',
            name='image',
            field=models.ImageField(null=True, upload_to='vips'),
        ),
    ]
