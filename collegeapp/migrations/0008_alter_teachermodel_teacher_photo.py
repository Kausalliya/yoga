# Generated by Django 4.1 on 2022-09-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0007_alter_teachermodel_teacher_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='Teacher_Photo',
            field=models.ImageField(blank=True, default='static/image/default.png', upload_to='image/'),
        ),
    ]