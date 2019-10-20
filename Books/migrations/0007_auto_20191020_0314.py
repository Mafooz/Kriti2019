# Generated by Django 2.2.6 on 2019-10-19 21:44

import Books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0006_books_is_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name_plural': 'Books'},
        ),
        migrations.AlterField(
            model_name='books',
            name='file',
            field=models.FileField(null=True, upload_to=Books.models.UploadedConfigPath),
        ),
    ]