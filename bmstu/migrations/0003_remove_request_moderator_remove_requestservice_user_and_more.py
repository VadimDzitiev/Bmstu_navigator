# Generated by Django 4.2.7 on 2023-11-22 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu', '0002_alter_request_options_alter_requestservice_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='moderator',
        ),
        migrations.RemoveField(
            model_name='requestservice',
            name='user',
        ),
        migrations.RemoveField(
            model_name='service',
            name='building',
        ),
        migrations.RemoveField(
            model_name='service',
            name='is_published',
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bmstu.userprofile', verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='service',
            name='buildings',
            field=models.BinaryField(blank=True, null=True, verbose_name='Фото строений'),
        ),
        migrations.AddField(
            model_name='service',
            name='is_deleted',
            field=models.BooleanField(default=True, verbose_name='Удалено'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_moderator',
            field=models.BooleanField(default=False, verbose_name='Модератор ли'),
        ),
        migrations.AlterField(
            model_name='request',
            name='completion_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='request',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='request',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[(1, 'Черновик'), (2, 'Удален'), (3, 'Сформирован'), (4, 'Завершен'), (5, 'Отклонен')], max_length=100, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='requestservice',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmstu.request', verbose_name='Заявка'),
        ),
        migrations.AlterField(
            model_name='requestservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmstu.service', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Маршрут'),
        ),
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='service',
            name='transition',
            field=models.BinaryField(blank=True, null=True, verbose_name='Фото маршрута'),
        ),
        migrations.AlterField(
            model_name='service',
            name='transition_time',
            field=models.CharField(max_length=100, verbose_name='Время перехода'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userpassword',
            field=models.CharField(max_length=100, verbose_name='Пароль'),
        ),
    ]
