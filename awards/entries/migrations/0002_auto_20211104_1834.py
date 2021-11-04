# Generated by Django 3.2.8 on 2021-11-04 15:34

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='entry_author',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='entry_text',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='entry_tittle',
        ),
        migrations.AddField(
            model_name='entry',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='entry',
            name='likecount',
            field=models.BigIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='entry',
            name='likes',
            field=models.ManyToManyField(related_name='projectlikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entry',
            name='livelink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entry',
            name='userpic',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('phonenumber', models.IntegerField(null=True)),
                ('bio', models.CharField(blank=True, max_length=255)),
                ('userpic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='Male', max_length=11)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('entry', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='entries.entry')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='entries.entry')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]