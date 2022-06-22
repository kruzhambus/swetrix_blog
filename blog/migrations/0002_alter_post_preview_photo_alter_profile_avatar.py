# Generated by Django 4.0.5 on 2022-06-22 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='preview_photo',
            field=models.ImageField(default='post_preview', upload_to='static/images/post_preview'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='yehor.jpg', upload_to='static/images/user_profiles_jpg'),
        ),
    ]