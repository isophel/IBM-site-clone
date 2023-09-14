# Generated by Django 4.2.5 on 2023-09-14 13:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Call_to_Action1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('link_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Call_to_Action2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('link_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Call_to_Action3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('link_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Final_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
                ('featured_image', models.ImageField(upload_to='images/')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('link_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('featured_image', models.ImageField(upload_to='images/')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecommededPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('featured_image', models.ImageField(upload_to='images/')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_text', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('link_text', models.CharField(max_length=100)),
                ('report_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='images/')),
                ('before_text', models.CharField(max_length=100)),
                ('on_hover_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Webcontent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Intro_text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Free_trial_text', models.CharField(max_length=100)),
                ('banner_video', models.FileField(upload_to='videos/')),
                ('video_caption', models.CharField(max_length=100)),
            ],
        ),
    ]