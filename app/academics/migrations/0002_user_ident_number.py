# Generated by Django 5.0.2 on 2024-03-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ident_number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
