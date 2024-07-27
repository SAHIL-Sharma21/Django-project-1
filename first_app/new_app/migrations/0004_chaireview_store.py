# Generated by Django 5.0.7 on 2024-07-26 15:28

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0003_chaivariety_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('chai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='new_app.chaivariety')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('chai_varieties', models.ManyToManyField(related_name='stores', to='new_app.chaivariety')),
            ],
        ),
    ]
