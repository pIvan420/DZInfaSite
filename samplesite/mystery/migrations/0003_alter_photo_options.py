# Generated by Django 4.1.3 on 2022-12-06 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystery', '0002_rubric_photo_rubric'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-published'], 'verbose_name': 'Заметка', 'verbose_name_plural': 'Заметки'},
        ),
    ]