# Generated by Django 3.1.7 on 2021-03-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0014_auto_20210330_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='q',
            field=models.IntegerField(default=0),
        ),
    ]