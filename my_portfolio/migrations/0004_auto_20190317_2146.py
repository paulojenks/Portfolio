# Generated by Django 2.1.7 on 2019-03-18 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0003_auto_20190317_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]