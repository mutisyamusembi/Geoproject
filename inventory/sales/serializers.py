from itertools import product
from rest_framework import serializers
from .models import Category, Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="item_category.name")

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    category_products = ProductSerializer(required=False, many=True)

    class Meta:
        model = Category
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.name")
    order_status = serializers.ReadOnlyField(source="order.status")
    total_value = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(
        required=False,
        many=True,
    )
    value = serializers.ReadOnlyField()
    order_id = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = "__all__"
