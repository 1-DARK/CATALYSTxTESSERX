# Generated by Django 5.2 on 2025-04-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('file', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
