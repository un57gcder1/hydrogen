# Generated by Django 2.2.7 on 2019-11-05 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the organization', max_length=80, unique=True)),
                ('description', models.TextField(default='', help_text='A description about the contest.')),
                ('group', models.ForeignKey(help_text='The group for users who want to modify', on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
    ]
