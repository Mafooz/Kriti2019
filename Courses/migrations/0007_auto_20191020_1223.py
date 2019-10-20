# Generated by Django 2.2.6 on 2019-10-20 06:53

import Courses.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0006_auto_20191020_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursesc',
            name='videos',
        ),
        migrations.AddField(
            model_name='videos',
            name='courses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='Courses.CoursesC'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='videos',
            field=models.FileField(null=True, upload_to=Courses.models.UploadedConfigPath),
        ),
    ]