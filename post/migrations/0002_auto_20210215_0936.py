# Generated by Django 3.0.6 on 2021-02-15 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='overview',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]