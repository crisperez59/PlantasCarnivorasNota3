# Generated by Django 2.2.6 on 2019-12-02 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMisFlores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=60)),
                ('tipoPlanta', models.CharField(max_length=20)),
                ('valor', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='plantas', verbose_name='imagen')),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
        migrations.AddField(
            model_name='cliente',
            name='prime',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]