# Generated by Django 3.2.8 on 2021-11-03 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20211103_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.restaurant')),
            ],
            options={
                'db_table': 'Waiter',
            },
        ),
    ]
