# Generated by Django 4.1.6 on 2023-02-06 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="boyd",
            new_name="body",
        ),
    ]
