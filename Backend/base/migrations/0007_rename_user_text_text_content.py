# Generated by Django 5.2 on 2025-04-21 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_text_alter_img_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='user_text',
            new_name='content',
        ),
    ]
