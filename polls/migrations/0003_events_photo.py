# Generated by Django 2.1.5 on 2019-03-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='cars'),
        ),
    ]
