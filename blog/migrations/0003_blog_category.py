# Generated by Django 3.1.7 on 2021-03-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210307_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default='uncategorized', max_length=100),
        ),
    ]