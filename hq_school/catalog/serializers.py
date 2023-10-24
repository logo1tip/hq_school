from rest_framework import serializers
from catalog.models import Product


class ProductStatisticSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    lesson_view_count = serializers.IntegerField()
    total_view_time = serializers.IntegerField()
    total_users_on_product = serializers.IntegerField()
    purchasing_percent = serializers.FloatField()

    class Meta:
        model = Product
        fields = (
            'title', 
            'lesson_view_count', 
            'total_view_time', 
            'total_users_on_product', 
            'purchasing_percent')