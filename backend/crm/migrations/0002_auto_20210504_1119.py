# Generated by Django 3.2 on 2021-05-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentbooking',
            options={'verbose_name': 'Комментарий (бронь)', 'verbose_name_plural': 'Комментарии (бронь)'},
        ),
        migrations.AlterModelOptions(
            name='commentcall',
            options={'verbose_name': 'Комментарий (звонки)', 'verbose_name_plural': 'Комментарии (звонки)'},
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.CharField(max_length=50, verbose_name='Дата поездки'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_quantity',
            field=models.CharField(max_length=200, verbose_name='Количество пассажиров'),
        ),
    ]