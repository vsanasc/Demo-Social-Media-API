# Generated by Django 3.2.8 on 2021-10-10 20:32

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Inactive'), (-1, 'Deleted')], default=1)),
                ('text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Inactive'), (-1, 'Deleted')], default=1)),
                ('state', models.PositiveSmallIntegerField(choices=[(1, 'Pending'), (2, 'Accepted'), (3, 'Rejected')], default=1)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_received', to=settings.AUTH_USER_MODEL)),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Inactive'), (-1, 'Deleted')], default=1)),
                ('text', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Inactive'), (-1, 'Deleted')], default=1)),
                ('file', models.FileField(upload_to='files')),
                ('is_image', models.BooleanField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
