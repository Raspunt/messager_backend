# Generated by Django 4.0.4 on 2022-05-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProg', '0002_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]