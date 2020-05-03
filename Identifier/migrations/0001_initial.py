# Generated by Django 3.0.5 on 2020-05-03 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activeStatus', models.BooleanField(default=True)),
                ('hashIdentifierString', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContentHash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentHashString', models.CharField(max_length=100)),
                ('hashIdentifierKey', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='Identifier.HashIdentifier')),
            ],
        ),
    ]
