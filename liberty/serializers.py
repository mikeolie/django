from rest_framework import serializers

from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Product:
        model = Products
        fields = ("date_added", "on_hold_till", "item_no", "description", "total_units", "is_featured", "price", "avg_cogs", "profit", "margin",
                  "mintage", "pop_known", "ngc_pop", "total_pop", "finer_known", "highlights", "attributes", "vendor", "categories", "display_y_n", "images_y_n")
