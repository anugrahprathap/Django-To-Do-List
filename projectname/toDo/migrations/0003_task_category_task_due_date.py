# Generated by Django 4.2.5 on 2023-10-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('High', 'High Priority'), ('Medium', 'Medium Priority'), ('Low', 'Low Priority'), ('None', 'No Priority')], default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]