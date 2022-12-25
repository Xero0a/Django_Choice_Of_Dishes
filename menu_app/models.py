from django.db import models


class MenuCategoriesModel(models.Model):
    """Таблица с категориями меню"""

    name_category = models.CharField(max_length=60, verbose_name="Категория")

    def __str__(self):
        return self.name_category

    class Meta:
        db_table = "menu_categories"
        verbose_name = "Категории меню"

class DishesModel(models.Model):
    """Таблица с блюдами"""

    name_dish = models.CharField(max_length=120, verbose_name="Блюдо")
    category = models.ForeignKey(MenuCategoriesModel, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    is_active = models.BooleanField(default=True, verbose_name="В наличии")   

    def __str__(self):
        return self.name_dish

    class Meta:
        db_table = "dishes"
        verbose_name = "Блюда"
