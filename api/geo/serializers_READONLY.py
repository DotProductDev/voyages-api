from rest_framework import serializers
from rest_framework.fields import SerializerMethodField,IntegerField,CharField
import re
from .models import *
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from django.core.exceptions import ObjectDoesNotExist

class LocationTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=LocationType
		fields='__all__'


class PolygonSerializer(serializers.ModelSerializer):
	class Meta:
		model=Polygon
		fields='__all__'

class LocationParentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Location
		fields='__all__'

class LocationChildSerializer(serializers.ModelSerializer):
	class Meta:
		model=Location
		fields='__all__'


class LocationSerializerDeep(serializers.ModelSerializer):
	parents=LocationParentSerializer(many=False)
	children=LocationChildSerializer(many=True)
	spatial_extent=PolygonSerializer(many=False)
	location_type=LocationTypeSerializer(many=False)
	class Meta:
		model=Location
		fields='__all__'

class LocationSerializer(serializers.ModelSerializer):
	spatial_extent=PolygonSerializer(many=False,allow_null=True)
	location_type=LocationTypeSerializer(many=False)
	latitude=serializers.DecimalField(allow_null=True,max_digits=10,decimal_places=7)
	longitude=serializers.DecimalField(allow_null=True,max_digits=10,decimal_places=7)
	class Meta:
		model=Location
		fields='__all__'