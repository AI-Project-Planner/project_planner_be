# Generated by Django 4.2.4 on 2023-08-31 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='saved',
            field=models.CharField(default='false', max_length=6),
        ),
    ]
