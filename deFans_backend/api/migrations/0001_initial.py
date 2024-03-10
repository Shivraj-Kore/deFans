# Generated by Django 4.0.10 on 2024-03-10 05:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=15, unique=True)),
                ('nickName', models.CharField(max_length=30)),
                ('bio', models.TextField(blank=True)),
                ('profilePhoto', models.ImageField(upload_to=None)),
                ('coverPhoto', models.ImageField(upload_to=None)),
                ('price', models.IntegerField()),
                ('walletAddress', models.CharField(max_length=42, unique=True, validators=[django.core.validators.RegexValidator(regex='^0x[a-fA-F0-9]{40}$')], verbose_name='Wallet Address')),
                ('subscribers', models.ManyToManyField(blank=True, related_name='subscribedTo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Creator',
                'verbose_name_plural': 'Creators',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=15, unique=True)),
                ('nickName', models.CharField(max_length=30)),
                ('bio', models.TextField(blank=True)),
                ('profilePhoto', models.ImageField(blank=True, upload_to=None)),
                ('coverPhoto', models.ImageField(blank=True, upload_to=None)),
                ('walletAddress', models.CharField(max_length=42, unique=True, validators=[django.core.validators.RegexValidator(regex='^0x[a-fA-F0-9]{40}$')], verbose_name='Wallet Address')),
                ('subscribed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creators', to='api.creator')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='CreatorPost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.FileField(upload_to='posts_content/%Y/%m/%d/')),
                ('caption', models.TextField(blank=True, max_length=200)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_posts', to='api.creator')),
            ],
            options={
                'verbose_name': 'CreatorPost',
                'verbose_name_plural': 'CreatorPosts',
            },
        ),
    ]
