from rest_framework import serializers
from main.models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta:
        model = Product, Review
        fields = "__all__"


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    class Meta:
        model = Product, Review
        fields = ["title", "description", "price", "reviews"]
