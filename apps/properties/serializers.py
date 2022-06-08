from rest_framework import serializers
from .models import Property, PropertyView
from django_countries.serializer_fields import CountryField




class PropertySerializer(serializers.ModelSerializer):
    country=CountryField(name_only=True)
    hosted_by=serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = ['id',
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
                  'photo1',
                  'photo2',
                  'photo3',
                  'photo4',
                  'photo5',
                  'availability_status',
                  'views']

    def get_hosted_by(self, obj):
        return obj.hosted_by.get_full_name()


class PropertyCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        exclude = ['pkid','views']


class PropertyViewSerializer(serializers.ModelSerializer):
    class Meta:
        models=PropertyView
        fields = ['id','ip_addr', 'property']

