from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from .models import EnquiryRequest


class EnquirySerializer(serializers.ModelSerializer):
    phone = PhoneNumberField()

    class Meta:
        model = EnquiryRequest
        fields = ["id", "names", "email", "phone", "message"]
