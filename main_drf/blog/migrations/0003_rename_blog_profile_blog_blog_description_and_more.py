# Generated by Django 4.2.2 on 2023-07-02 18:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_profile',
            new_name='blog_description',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_file',
        ),
        migrations.RemoveField(
            model_name='post',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='blog',
            field=models.ManyToManyField(related_name='tags', to='blog.post'),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comment_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
