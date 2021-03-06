# Generated by Django 2.1.4 on 2019-01-30 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year_released', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('birth_date', models.CharField(default='', max_length=100)),
                ('biggest_hit', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song_Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Album')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Song')),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='albums',
            field=models.ManyToManyField(blank=True, through='history.Song_Album', to='history.Album'),
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Artist'),
        ),
        migrations.AlterUniqueTogether(
            name='song_album',
            unique_together={('album', 'song')},
        ),
    ]
