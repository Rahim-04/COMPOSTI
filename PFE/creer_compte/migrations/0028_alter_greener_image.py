# Generated by Django 4.1.7 on 2023-05-15 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creer_compte', '0027_alter_greener_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greener',
            name='image',
            field=models.ImageField(upload_to='static\\images\\profile_pics\\profil.png'),
        ),
    ]
