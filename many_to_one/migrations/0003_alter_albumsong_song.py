# Generated by Django 4.1 on 2022-09-30 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_one', '0002_remove_song_album_remove_song_singer_albumsong'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumsong',
            name='song',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='many_to_one.song'),
        ),
    ]
