# Generated by Django 2.2.6 on 2019-10-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_auto_20191019_1535'),
        ('Clubs', '0002_auto_20191019_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubs',
            name='Courses',
        ),
        migrations.AddField(
            model_name='clubs',
            name='Courses',
            field=models.ManyToManyField(related_name='clubs', to='Courses.Courses'),
        ),
    ]
