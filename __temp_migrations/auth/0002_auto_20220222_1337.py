# Generated by Django 2.2.12 on 2022-02-22 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permission',
            options={'ordering': ('content_type__app_label', 'content_type__model', 'codename'), 'verbose_name': 'permission', 'verbose_name_plural': 'permissions'},
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
