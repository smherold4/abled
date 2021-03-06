# Generated by Django 2.0.6 on 2018-07-15 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_candidate_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('filetype', models.CharField(max_length=250)),
                ('filesize', models.IntegerField()),
                ('fileurl', models.CharField(max_length=450)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='app.Candidate')),
            ],
        ),
    ]
