# Generated by Django 4.1.3 on 2022-12-06 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mystery.rubric', verbose_name='Рубрика'),
        ),
    ]
