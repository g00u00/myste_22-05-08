# Generated by Django 4.0.4 on 2022-05-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_abc_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='abc',
            name='pub_date',
            field=models.DateTimeField(default='2022-05-10', verbose_name='date published'),
        ),
    ]
