# Generated by Django 4.2.2 on 2023-06-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('trips', '0003_trip_driver_rider'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_set', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='status',
            field=models.CharField(choices=[('REQUESTED', 'REQUESTED'), ('STARTED', 'STARTED'), ('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETED', 'COMPLETED')], default='REQUESTED', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]