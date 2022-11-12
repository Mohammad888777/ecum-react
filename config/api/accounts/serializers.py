from rest_framework import serializers
from .models import User


class UserSserialzier(serializers.ModelSerializer):

    class Meta:

        extra_kwargs={"password":{"write_only":True}}
        model=User
        fields=["first_name","password","username","last_name","email","phone_number","last_login","date_joined","is_admin","is_active","is_staff"]

    def create(self, validated_data):

        password=validated_data.get("password",None)
        instance=User(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance
    
    def update(self, instance, validated_data):

        password=validated_data.get("password",None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

        