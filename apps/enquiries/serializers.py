from rest_framework import serializers
from .models import EnquiryRequest
from phonenumber_field.serializerfields import PhoneNumberField



class EnquirySerializer(serializers.ModelSerializer):
    phone= PhoneNumberField()

    class Meta:
        model = EnquiryRequest
        fields = ['id','names', 'email', 'phone','message']