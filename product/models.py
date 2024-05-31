from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=50, default='')
    cost = models.DecimalField(verbose_name='Цена', default=0.00, max_digits=7, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    discount = models.DecimalField(verbose_name='Скидка в %', default=0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    url_path = models.URLField(verbose_name='Ссылка на товар', default='', null=True)
    url_img = models.URLField(verbose_name='Ссылка на изображение', default='', null=True)
    image = models.ImageField(verbose_name='Изображение',upload_to='img_product')
    article = models.CharField(verbose_name='Артикуль', max_length=50, default='')
    gender = models.CharField(verbose_name='Пол', max_length=50, default='')
    country = models.CharField(verbose_name='Страна', max_length=50, default='')
    waterproof = models.CharField(verbose_name='Водостойкость', max_length=50, default='')
    type_mechanism = models.CharField(verbose_name='Тип механизма', max_length=50, default='')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'
    # def get_absolute_url(self):
    #     return f'/news/{self.id}'
    # def display_id(self):
    #     return f"{self.id:05}"

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})
    def sell_price(self):
        if self.discount:
            return round(self.cost - self.cost * self.discount/100, 2)
        return self.cost
    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        # ordering = ['-quantity']
