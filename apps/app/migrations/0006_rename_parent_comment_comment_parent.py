# Generated by Django 5.0.7 on 2024-08-08 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_commentlike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parent_comment',
            new_name='parent',
        ),
    ]