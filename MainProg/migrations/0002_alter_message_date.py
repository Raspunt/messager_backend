# Generated by Django 4.0.4 on 2022-05-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]