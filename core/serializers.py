from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Userseralizer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    confirm_password=serializers.CharField(write_only=True)
    role=serializers.ChoiceField(choices=User.ROLE_CHOICES)
    class Meta:
        model=User
        fields=['id','username','email','role','password','confirm_password']
        extra_kwargs = {'id': {'read_only': True}}
        
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)