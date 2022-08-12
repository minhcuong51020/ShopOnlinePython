# Generated by Django 4.0.3 on 2022-03-21 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('electronic', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoes', '0001_initial'),
        ('book', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='bookItem',
            field=models.ManyToManyField(to='book.bookitem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='electronicItem',
            field=models.ManyToManyField(to='electronic.electronicitem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order'),
        ),
        migrations.AddField(
            model_name='cart',
            name='shoesItem',
            field=models.ManyToManyField(to='shoes.shoesitem'),
        ),
    ]