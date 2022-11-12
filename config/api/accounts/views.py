from cgitb import lookup
from django.shortcuts import render
from .serializers import UserSserialzier
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .utils import generate_token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout,authenticate
from rest_framework import viewsets
import re



@csrf_exempt
def signin(request):

    if request.method !="POST":
        return JsonResponse({"error":"mehtod allowed is post only"})
    
    email=request.POST.get("email")
    password=request.POST.get("password")

    if password:
        if len(password)<=3:
            return JsonResponse({"error":"length of password is low"})

    User=get_user_model()

    try:

        user=User.objects.get(email=email)

        if user.check_password(password):

            user_dict=User.objects.filter(email=email).values().first()
            user_dict.pop("password")
        

            if user.session_token!="0":
                user.session_token="0"
                user.save()
                return JsonResponse({"error":"previous session is exsist"})

            token=generate_token()
            user.session_token=token
            user.save()
            login(request,user)

            return JsonResponse({"token":token,"msg":"you are logged in","user_dict":user_dict})
        else:
            return JsonResponse({"error":"password is incorrect "})




    except User.DoesNotExist:

        return JsonResponse({"error":"user does not exist"})



def signout(request,pk):

    logout(request)
    UserModel=get_user_model()
    user=UserModel.objects.get(pk=pk)
    if user:
        user.session_token="0"
        user.save()

    return JsonResponse({"msg":"you logged put"})
    

    
    


    
    



class UserViewSet(viewsets.ModelViewSet):


    serializer_class=UserSserialzier
    permission_classes_by_action={"create":[AllowAny]}
    queryset=get_user_model().objects.all().order_by("-id")

    def get_permissions(self):
        
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError :
            return [permission() for permission in self.permission_classes]

    
    def perform_create(self, serializer):

        serializer.save()





