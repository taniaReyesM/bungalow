import logging

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from houses.models import House
from houses.utils import format_price, transform_params
from rest_framework import serializers
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('area_unit', 'bathrooms', 'bedrooms', 'home_size',
                  'home_type', 'last_sold_date', 'last_sold_price', 'link',
                  'price', 'property_size', 'rent_price',
                  'rentzestimate_amount', 'rentzestimate_last_updated',
                  'tax_value', 'tax_year', 'year_built', 'zestimate_amount',
                  'zestimate_last_updated', 'zillow_id', 'address', 'city',
                  'state', 'zipcode', 'format_price')

    format_price = serializers.SerializerMethodField()

    def get_format_price(self, obj):
        return format_price(obj.price)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_house_by_id(request, house_id):
    try:
        house = House.objects.get(pk=house_id)
        serializer = HouseSerializer(house, context={'request': request})
        return Response([serializer.data])
    except House.DoesNotExist:
        return JsonResponse({'error': "Property Not Found"}, status=404)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_houses_by_params(request):
    query_params = transform_params(request.GET)
    houses = House.objects.filter(**query_params)
    serializer = HouseSerializer(houses,
                                 many=True,
                                 context={'request': request})
    return Response([serializer.data])
