# Generated by Django 4.2.15 on 2024-08-26 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='models.level'),
        ),
    ]
