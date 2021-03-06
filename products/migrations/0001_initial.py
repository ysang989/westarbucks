# Generated by Django 4.0.4 on 2022-05-08 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allegy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'allegy',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_name', models.CharField(max_length=45)),
                ('english_name', models.CharField(max_length=45)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'db_table': 'drink',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('size_ml', models.CharField(max_length=45)),
                ('size_fluid_ounce', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Nutritions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kca', models.DecimalField(decimal_places=2, max_digits=12)),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=12)),
                ('saturated_fag_g', models.DecimalField(decimal_places=2, max_digits=12)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=12)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=12)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=12)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.sizes')),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
        migrations.CreateModel(
            name='Allegy_drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allegy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.allegy')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
            ],
            options={
                'db_table': 'allegy_drink',
            },
        ),
    ]
