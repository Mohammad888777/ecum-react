from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=Order
        # fields=["product_name","user","total_products",'transaction_id','total_amount']
        fields=["user"]