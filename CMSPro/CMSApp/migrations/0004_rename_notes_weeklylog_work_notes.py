# Generated by Django 5.1.3 on 2024-11-20 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMSApp', '0003_weeklylog_delete_dailylog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklylog',
            old_name='notes',
            new_name='work_notes',
        ),
    ]
