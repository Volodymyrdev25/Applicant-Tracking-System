# Generated by Django 4.2.3 on 2024-02-15 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_studentclassroom_slug'),
        ('assignment', '0010_remove_quiz_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolvedQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('date_solved', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentprofile')),
            ],
        ),
    ]
