# Generated by Django 4.1.7 on 2023-02-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_event_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AlterField(
            model_name='event',
            name='Event_title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]