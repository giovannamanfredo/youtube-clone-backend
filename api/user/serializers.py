from rest_framework import serializers
from .models import Creator

user = [
            "last_login",
            "is_superuser",
            "username",
            "is_staff",
            "is_active",
            "date_joined",
            "first_name",
            "last_name",
            "email",
            "channel_name",
            "is_channel_active",
            "date_of_birth",
            "profile_link",
            "cover_link",
            "groups",
            "user_permissions"
        ]

class CreateCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = user
        
class UpdateCreatorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    date_of_birth = serializers.DateField(required=False)
    channel_name = serializers.CharField(required=False)
    
    
    class Meta:
        model = Creator
        exclude = [
            "id",
            "email",
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
	        "is_active",
            "date_joined",
            "is_channel_active",
            ]