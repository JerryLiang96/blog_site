# Generated by Django 2.2.3 on 2019-09-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ManyToManyField(blank=True, to='blog.Image'),
        ),
    ]
