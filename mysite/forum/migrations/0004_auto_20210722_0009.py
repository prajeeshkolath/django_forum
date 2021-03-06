# Generated by Django 2.2.10010 on 2021-07-22 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20210719_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='topic_id',
            new_name='topic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thread_id',
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Thread'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='forum.Category'),
        ),
    ]
