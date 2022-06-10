from rest_framework import serializers
from .models import Property, PropertyView
from django_countries.serializer_fields import CountryField




class PropertySerializer(serializers.ModelSerializer):
    country=CountryField(name_only=True)
    hosted_by=serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = ['id',
                  'slug',
                  'title',
                  'hosted_by',
                  'description',
                  'ref_code',
                  'postal_code',
                  'price',
                  'country',
                  'city',
                  'street_address',
                  'property_number',
                  'plot_area',
                  'total_floors',
                  'num_of_bedrooms',
                  'num_of_bathrooms',
                  'amenities',
                  'advert_type',
                  'property_type',
                  'cover_photo',
                  'photo1',
                  'photo2',
                  'photo3',
                  'photo4',
                  'photo5',
                  'availability_status',
                  'views']

    def get_hosted_by(self, obj):
        first_name= obj.hosted_by.first_name
        last_name = obj.hosted_by.last_name
        return f"{first_name} {last_name}"


class PropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        exclude = ['pkid', 'created_at','update_at','views', 'ref_code', 'hosted_by']


class PropertyViewSerializer(serializers.ModelSerializer):
    class Meta:
        models=PropertyView
        fields = ['id','ip_addr', 'property']

