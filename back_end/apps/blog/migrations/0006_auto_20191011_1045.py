# Generated by Django 2.2.3 on 2019-10-11 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190918_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='describe',
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(blank=True, upload_to='back_end/static/image/full_size'),
        ),
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.FilePathField(path='/back_end/static/image/thumb'),
        ),
    ]