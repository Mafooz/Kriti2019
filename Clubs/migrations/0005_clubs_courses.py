# Generated by Django 2.2.6 on 2019-10-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0004_auto_20191019_1728'),
        ('Clubs', '0004_auto_20191019_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubs',
            name='courses',
            field=models.ManyToManyField(related_name='clubs', to='Courses.CoursesC'),
        ),
    ]