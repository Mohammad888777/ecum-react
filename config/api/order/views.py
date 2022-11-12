from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt



def validate_user(id,token):

    UserModel=get_user_model()
    try:
        user=UserModel.objects.get(pk=id)
        if user.session_token==token:
            return True
        return False

    except UserModel.DoesNotExist:

        return JsonResponse({"error":"user not found"})




@csrf_exempt
def make_order(request,id,token):

    if not validate_user(id,token):
        return JsonResponse({"error":"token or user is invalid"})

    if request.method=="POST":

        transaction_id=request.POST["transaction_id"]
        amount=request.POST["amount"]
        products=request.POST["products"]
        total_pro=len(products.split(','))
        UserModel=get_user_model()

        try:
            user=UserModel.objects.get(pk=id)

        except UserModel.DoesNotExist:

            return JsonResponse({"error":"user does not exsits"})
        order=Order(
            user=user,product_names=products,total_products=total_pro,
            transaction_id=transaction_id,total_amount=amount
        )
        order.save()
        return JsonResponse({"success":True,"msg":"your order is made"})


class OrderViewSet(viewsets.ModelViewSet):
    
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
