# Generated by Django 3.0.3 on 2020-03-13 16:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0012_userexteded'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserExteded',
            new_name='UserExtended',
        ),
    ]