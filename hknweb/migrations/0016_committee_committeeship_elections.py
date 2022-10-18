# Generated by Django 2.2.8 on 2022-05-19 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursesemester', '0002_auto_20210202_0225'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hknweb', '0015_candidateprovisioningpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Elections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursesemester.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Committeeship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('committee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hknweb.Committee')),
                ('elections', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hknweb.Elections')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]