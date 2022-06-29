from uuid import uuid4
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your models here.

ORDER_STATUS = (
    ("PENDING", "Pending"),
    ("ACTIVE", "Active"),
    ("PAID", "Paid"),
    ("CANCELLED", "Cancelled"),
)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ("name", "description")


class Product(models.Model):
    item_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_products"
    )
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("item_category", "name")


class Order(models.Model):
    status = models.CharField(max_length=100, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.order_id

    @property
    def value(self):

        order_items = self.order_items.all()
        return (
            order_items.aggregate(Sum("total_value"))["total_value__sum"]
            if order_items.exists()
            else 0.00
        )

    @property
    def order_id(self):
        uid = uuid4()
        short_uid = str(uid)[:4]
        return str(timezone.now().date()) + short_uid


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    qty = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    total_value = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def get_total_value(self):
        self.total_value = self.qty * self.product.price

    def update_product_stock(self):
        if self.qty > self.product.stock:
            raise ValidationError(
                {
                    "qty": "The quantity cannot be more than current stock of {}".format(
                        self.product.stock
                    )
                }
            )
        else:
            self.product.stock -= self.qty
            self.product.save()

    def save(self, *args, **kwargs):
        self.update_product_stock()
        self.get_total_value()
        super().save(*args, **kwargs)
        self.order.save()

    class Meta:
        unique_together = ("order", "product")
