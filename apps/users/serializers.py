from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")
    profile_image = serializers.ImageField(source="profile.profile_img")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    bio = serializers.CharField(source="profile.about_me")
    full_names = serializers.SerializerMethodField(source="get_full_name")

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "phone",
            "gender",
            "profile_image",
            "country",
            "city",
            "bio",
            "full_names",
        ]

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "email", "first_name", "last_name", "phone", "password"]
