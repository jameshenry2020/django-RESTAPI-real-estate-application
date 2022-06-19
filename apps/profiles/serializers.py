from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from .models import HostAgent, Profile


class AgentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostAgent
        fields = ["brand_name", "license", "office_address"]


class AgentProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="agent.user.first_name")
    last_name = serializers.CharField(source="agent.user.last_name")
    email = serializers.EmailField(source="agent.user.email")
    profile_img = serializers.ImageField(source="agent.profile_img")
    full_name = serializers.SerializerMethodField(read_only=True)
    phone = PhoneNumberField(source="agent.user.phone")
    country = CountryField(name_only=True)

    class Meta:
        model = HostAgent
        fields = [
            "brand_name",
            "license",
            "first_name",
            "last_name",
            "email",
            "full_name",
            "phone",
            "country",
            "gender",
            "about_me",
            "profile_img",
            "city",
            "office_address",
            "num_of_reviews",
        ]

    def get_full_name(self, obj):
        first_name = obj.agent.user.first_name.title()
        last_name = obj.agent.user.last_name.title()
        return f"{first_name} {last_name}"


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(source="user.id")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    phone = PhoneNumberField(source="user.phone")
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = [
            "user_id",
            "first_name",
            "last_name",
            "email",
            "full_name",
            "phone",
            "country",
            "gender",
            "about_me",
            "profile_img",
            "city",
            "is_agent",
        ]

    def get_full_name(self, obj):
        return f"{obj.user.first_name.title()} {obj.user.last_name.title()}"


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = ["about_me", "gender", "profile_img", "country", "city"]
