# Generated by Django 4.0.4 on 2022-05-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_abc_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abc',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
        migrations.AddField(
            model_name='abc',
            name='pub_date',
            field=models.DateTimeField(default='2000-00-00', verbose_name='date published'),
        ),
    ]
