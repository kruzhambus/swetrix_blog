# Generated by Django 4.0.5 on 2022-06-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_email_alter_comment_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='preview_photo',
            field=models.ImageField(default='Screenshot_from_2022-06-23_08-57-42.png', upload_to='static/images/post_preview'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='Screenshot_from_2022-06-22_03-57-39.png', upload_to='static/images/user_profiles_jpg'),
        ),
    ]