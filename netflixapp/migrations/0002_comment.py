# Generated by Django 3.2.5 on 2021-07-26 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('body', models.TextField()),
                ('comment_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='netflixapp.comment')),
                ('netflix_id', models.ForeignKey(db_column='netflix_id', on_delete=django.db.models.deletion.CASCADE, to='netflixapp.netflix')),
            ],
        ),
    ]
