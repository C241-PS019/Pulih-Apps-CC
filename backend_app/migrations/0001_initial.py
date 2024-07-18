# Generated by Django 5.0.6 on 2024-07-18 15:38

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Akun',
            fields=[
                ('user_uid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('identifier', models.EmailField(max_length=254)),
                ('providers', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now=True)),
                ('signed_in', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Konselor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nama_panggilan', models.CharField(max_length=20)),
                ('mitra', models.CharField(max_length=50)),
                ('telepon', models.CharField(blank=True, max_length=20, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('akun', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend_app.akun')),
            ],
        ),
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nama_panggilan', models.CharField(max_length=20)),
                ('nim', models.CharField(max_length=20)),
                ('universitas', models.CharField(max_length=50)),
                ('telepon', models.CharField(blank=True, max_length=15, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('akun', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend_app.akun')),
            ],
        ),
        migrations.CreateModel(
            name='Konseling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=50)),
                ('tempat', models.CharField(max_length=50)),
                ('tanggal', models.DateField()),
                ('waktu', models.TimeField()),
                ('pesan', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(choices=[('disetujui', 'disetujui'), ('diproses', 'diproses'), ('selesai', 'selesai'), ('reschedule', 'reschedule')], default='diproses', max_length=10)),
                ('konselor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_app.konselor')),
                ('pengguna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_app.pengguna')),
            ],
        ),
        migrations.CreateModel(
            name='JurnalSore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('tanggal', models.DateField(default=datetime.date.today)),
                ('q1', models.CharField(max_length=20)),
                ('q2', models.CharField(max_length=20)),
                ('q3', models.CharField(max_length=20)),
                ('q4', models.CharField(max_length=20)),
                ('q5', models.CharField(max_length=20)),
                ('pengguna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_app.pengguna')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JurnalPagi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('tanggal', models.DateField(default=datetime.date.today)),
                ('q1', models.CharField(max_length=20)),
                ('q2', models.CharField(max_length=20)),
                ('q3', models.CharField(max_length=20)),
                ('q4', models.CharField(max_length=20)),
                ('pengguna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_app.pengguna')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
