from rest_framework import serializers

from .models import Products


class ProductSerializer(serializers.Serializer):
    date_added = serializers.DateTimeField
    item_no = serializers.CharField
    on_hold_till = serializers.DateTimeField
    description = serializers.CharField
    total_units = serializers.IntegerField
    is_featured = serializers.BooleanField
    price = serializers.DecimalField
    avg_cogs = serializers.DecimalField
    profit = serializers.DecimalField
    margin = serializers.DecimalField
    mintage = serializers.IntegerField
    pop_known = serializers.CharField
    ngc_pop = serializers.IntegerField
    pcgs_pop = serializers.IntegerField
    total_pop = serializers.IntegerField
    finer_known = serializers.IntegerField 
    highlights = serializers.ListField()
    attributes= serializers.ListField()
    vendor = serializers.CharField
    categories = serializers.ReadOnlyField()
    display_y_n = serializers.CharField
    images_y_n = serializers.CharField

    class ProductSerializer:
        model = Products
        fields = ("__all__")