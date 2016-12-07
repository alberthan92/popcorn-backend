# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daum_id', models.IntegerField(unique=True)),
                ('name_kor', models.CharField(max_length=100)),
                ('name_eng', models.CharField(blank=True, max_length=100)),
                ('profile_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BoxOfficeMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('rank', models.IntegerField(default=0)),
                ('release_date', models.DateField()),
                ('ticketing_rate', models.FloatField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('star', models.FloatField(choices=[(0.0, 0), (0.5, 0.5), (1.0, 1), (1.5, 1.5), (2.0, 2), (2.5, 2.5), (3.0, 3), (3.5, 3.5), (4.0, 4), (4.5, 4.5), (5.0, 5)])),
                ('content', models.CharField(blank=True, max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daum_id', models.IntegerField(unique=True)),
                ('name_kor', models.CharField(max_length=100)),
                ('name_eng', models.CharField(max_length=100)),
                ('profile_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FamousLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FamousLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=100)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Actor')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FamousLineAuthor', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(through='movie.FamousLike', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('mag_id', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('img_url', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MakingCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('making_country', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daum_id', models.IntegerField(unique=True)),
                ('title_kor', models.CharField(max_length=100)),
                ('title_eng', models.CharField(blank=True, max_length=100)),
                ('star_sum', models.FloatField(default=0.0)),
                ('comment_count', models.IntegerField(default=0)),
                ('star_average', models.FloatField(default=0.0)),
                ('created_year', models.IntegerField()),
                ('img_url', models.TextField()),
                ('main_trailer', models.TextField()),
                ('videos', models.TextField()),
                ('run_time', models.CharField(max_length=30)),
                ('synopsis', models.TextField()),
                ('Release_date', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=30)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(through='movie.MovieActor', to='movie.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(to='movie.Director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='movie.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Grade'),
        ),
        migrations.AddField(
            model_name='movie',
            name='making_country',
            field=models.ManyToManyField(to='movie.MakingCountry'),
        ),
        migrations.AddField(
            model_name='famousline',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='famouslike',
            name='famous_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.FamousLine'),
        ),
        migrations.AddField(
            model_name='famouslike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='like_users',
            field=models.ManyToManyField(related_name='comment_set_like_users', through='movie.CommentLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='boxofficemovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie'),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('author', 'movie')]),
        ),
    ]
