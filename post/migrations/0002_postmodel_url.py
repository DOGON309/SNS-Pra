# Generated by Django 3.2.4 on 2021-07-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
