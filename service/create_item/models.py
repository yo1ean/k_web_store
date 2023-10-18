from django.db import models
from django.urls import reverse


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('F', 'Female'),
        ('M', "Male")
    )
    type = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default='M')
    slug = models.SlugField(max_length=10, unique=True)

    class Meta:
        ordering = ('type', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('shop:products_category', args=[self.slug])


class Product(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','X-Large'),
        ('XXL','XX-Large'),
        ('XXXL','XXX-Large'),
    )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000, blank=True)
    available = models.BooleanField(default=True)
    size = models.CharField(max_length=4, choices=SIZE_CHOICES, default='Small')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return f"Item created: {self.name}, {self.size} with price {self.price}€"

    def get_absolute_url(self):
        return reverse('item:product_detail', args=[self.slug])