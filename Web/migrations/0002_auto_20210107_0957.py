# Generated by Django 3.1.4 on 2021-01-07 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='Images',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='city',
            name='shortDescribtion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
