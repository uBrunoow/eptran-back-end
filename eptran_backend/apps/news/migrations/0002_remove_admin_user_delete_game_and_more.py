# Generated by Django 4.2.6 on 2024-06-08 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="admin",
            name="user",
        ),
        migrations.DeleteModel(
            name="Game",
        ),
        migrations.RemoveField(
            model_name="gamestatistics",
            name="game",
        ),
        migrations.RemoveField(
            model_name="gamestatistics",
            name="user",
        ),
        migrations.RemoveField(
            model_name="staff",
            name="user",
        ),
        migrations.RemoveField(
            model_name="student",
            name="user",
        ),
        migrations.RemoveField(
            model_name="user",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="user",
            name="user_permissions",
        ),
        migrations.AlterField(
            model_name="news",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="news_posts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="savednews",
            name="news",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="news.news"
            ),
        ),
        migrations.AlterField(
            model_name="savednews",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="saved_news",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="Admin",
        ),
        migrations.DeleteModel(
            name="GameStatistics",
        ),
        migrations.DeleteModel(
            name="Staff",
        ),
        migrations.DeleteModel(
            name="Student",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
