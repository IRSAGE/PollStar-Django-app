# Generated by Django 3.1.7 on 2021-04-06 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='queston',
            new_name='question',
        ),
    ]
