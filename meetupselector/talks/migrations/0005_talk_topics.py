# Generated by Django 3.2.16 on 2022-10-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0004_talk_speakers'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='topics',
            field=models.ManyToManyField(related_name='talks', to='talks.Topic', verbose_name='topics'),
        ),
    ]
