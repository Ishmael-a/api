from rest_framework import serializers
from .models import Category, Region, Product, Cart
import base64


class Base64ImageField(serializers.ImageField):
    def to_representation(self, value):
        if value:
            return base64.b64encode(value).decode('utf-8')
        return None

    def to_internal_value(self, data):
        return data


class CategorySerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']

    def create(self, validated_data):
        image_data = validated_data.pop('image', None)
        category = Category.objects.create(**validated_data)
        if image_data:
            category.image = image_data.read()
            category.save()
        return category


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name', queryset=Category.objects.all())
    region = serializers.SlugRelatedField(
        slug_field='name', queryset=Region.objects.all())
    image = Base64ImageField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',
                  'stock_quantity', 'category', 'region', 'image']

    def create(self, validated_data):
        image_data = validated_data.pop('image', None)
        product = Product.objects.create(**validated_data)
        if image_data:
            product.image = image_data.read()
            product.save()
        return product


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'product', 'product_id', 'quantity']
