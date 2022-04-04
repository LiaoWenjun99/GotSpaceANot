# Generated by Django 4.0.3 on 2022-04-04 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('level', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'level',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('library_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('library_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'library',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seat_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('row', models.CharField(blank=True, max_length=1, null=True)),
                ('col', models.CharField(blank=True, max_length=1, null=True)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='booking.level')),
                ('library', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='booking.library')),
            ],
            options={
                'db_table': 'seat',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Occupied',
            fields=[
                ('occupied_id', models.AutoField(primary_key=True, serialize=False)),
                ('matric_no', models.CharField(blank=True, max_length=9, null=True)),
                ('book_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='booking.level')),
                ('library', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='booking.library')),
                ('seat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='booking.seat')),
            ],
            options={
                'db_table': 'occupied',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='level',
            name='library',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='booking.library'),
        ),
    ]
