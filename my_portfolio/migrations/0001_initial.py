# Generated by Django 2.1.7 on 2019-03-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144)),
                ('description', models.TextField()),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField()),
            ],
        ),
    ]
