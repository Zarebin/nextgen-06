# Generated by Django 4.2 on 2023-04-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='browser_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser', models.CharField(max_length=50)),
                ('visitsCount', models.IntegerField(default=1)),
            ],
        ),
    ]
