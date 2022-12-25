# Generated by Django 4.1.4 on 2022-12-25 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuCategoriesModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_category",
                    models.CharField(max_length=60, verbose_name="Категория"),
                ),
            ],
            options={
                "verbose_name": "Категории меню",
                "db_table": "menu_categories",
            },
        ),
        migrations.CreateModel(
            name="DishesModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_dish", models.CharField(max_length=120, verbose_name="Блюдо")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="Цена"
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="В наличии"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="menu_app.menucategoriesmodel",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Блюда",
                "db_table": "dishes",
            },
        ),
    ]