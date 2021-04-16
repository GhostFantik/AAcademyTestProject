from rest_framework import serializers
from core.models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    """Serializer for specific resource"""
    cost = serializers.SerializerMethodField()
    price = serializers.FloatField()
    amount = serializers.FloatField()

    class Meta:
        model = Resource
        fields = ['title', 'id', 'amount', 'unit', 'price', 'date', 'cost']

    def get_cost(obj):
        return obj.price * obj.amount


class AllResourcesSerializer(serializers.Serializer):
    """Serializer for display all resources"""
    resources = serializers.SerializerMethodField()
    total_count = serializers.SerializerMethodField()

    def get_total_count(self, obj):
        return len(obj)

    def get_resources(self, obj):
        return ResourceSerializer(obj, many=True)
