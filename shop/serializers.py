from rest_framework import serializers

from .models import Item, Category, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        new_category = Category(
            name=validated_data['name'],
        )
        new_category.save()
        return new_category


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['category', ]
        # read_only_fields = ['category', 'profile', ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        # read_only_fields = ['item', 'profile']
