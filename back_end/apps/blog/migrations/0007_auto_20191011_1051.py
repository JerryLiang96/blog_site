# Generated by Django 2.2.3 on 2019-10-11 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191011_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.FilePathField(path='back_end/static/image/thumb'),
        ),
    ]