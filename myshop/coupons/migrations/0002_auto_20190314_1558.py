# Generated by Django 2.1.7 on 2019-03-14 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='vaild_form',
            new_name='vaild_from',
        ),
    ]
