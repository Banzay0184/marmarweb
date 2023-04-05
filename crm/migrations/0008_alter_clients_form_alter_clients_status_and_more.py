# Generated by Django 4.0.2 on 2022-08-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_alter_clients_form_alter_clients_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='form',
            field=models.CharField(choices=[('Instagram', 'Instagram'), ('Facebook', 'Facebook')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='status',
            field=models.CharField(choices=[('Встреча', 'Встреча'), ('Договор', 'Договор'), ('Архив', 'Архив'), ('Ожиданы', 'Ожиданы')], default='Ожиданы', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Оплачено', 'Оплачено'), ('Аванс', 'Аванс'), ('Ожидание', 'Ожидание')], default='Ожидание', max_length=120),
        ),
    ]
