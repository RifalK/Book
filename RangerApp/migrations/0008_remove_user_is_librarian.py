# Generated by Django 4.2.11 on 2024-03-15 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RangerApp', '0007_event_rename_name_category_cname_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_librarian',
        ),
    ]
