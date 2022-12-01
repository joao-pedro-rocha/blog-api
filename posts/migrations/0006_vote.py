# Generated by Django 4.1.3 on 2022-12-01 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=7, verbose_name='Opção')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.comment', verbose_name='Comentário')),
            ],
        ),
    ]