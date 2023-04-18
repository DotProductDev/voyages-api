from __future__ import unicode_literals

from builtins import str

from django.db import models
from django.db.models import Prefetch
# from voyage.models import NamedModelAbstractBase
#from django.utils.translation import gettext_lazy as _

class GeoUid(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.CharField(max_length=1000, null=False, blank=False, unique=True)

class Route(models.Model):
	"""
	Route json store
	"""
	source=models.ForeignKey(
		'Location',
		verbose_name="Alice",
		null=False,
		on_delete=models.CASCADE,
		related_name='sourceofroute'
	)
	target=models.ForeignKey(
		'Location',
		verbose_name="Bob",
		null=False,
		on_delete=models.CASCADE,
		related_name='targetofroute'
	)
	dataset= models.IntegerField(
		"Dataset",
		null=False,
		blank=False
	)
	shortest_route=models.JSONField(
		"Endpoint to endpoint route",
		null=True
	)
	class Meta:
		unique_together=(['source','target','dataset'])
		verbose_name = "Route"
		verbose_name_plural = "Routes"

class Adjacency(models.Model):
	"""
	Simplified network linkages -- simple a/b connections
	"""
	source=models.ForeignKey(
		'Location',
		verbose_name="Alice",
		null=False,
		on_delete=models.CASCADE,
		related_name='sourceof'
	)
	target=models.ForeignKey(
		'Location',
		verbose_name="Bob",
		null=False,
		on_delete=models.CASCADE,
		related_name='targetof'
	)
	dataset= models.IntegerField(
		"Dataset",
		null=True
	)
	
	distance=models.DecimalField(
		"Distance",
		null=True,
		blank=True,
		max_digits=8,
		decimal_places=5
	)
	
	class Meta:
		unique_together=(['source','target','dataset'])
		verbose_name = "Location Adjacency"
		verbose_name_plural = "Location Adjacencies"
	
class Polygon(models.Model):
	"""
	Shape of a spatial entity (optional for the locations that link to these)
	"""
	shape=models.JSONField(
		"Geojson Polygon",
		null=True
		)

# Voyage Regions and Places
class LocationType(models.Model):
	"""
	Geographic Location Type
	We will default to points, but open up onto a polygons model for when we want to show countries etc
	"""
	name = models.CharField(
		"Geographic Location Type",
		max_length=255,
		unique=True,
		blank=False,
		null=False
	)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Geographic Location Type"
		verbose_name_plural = "Geographic Location Types"

# Voyage Regions and Places
class Location(models.Model):
	"""
	Geographic Location
	"""

	name = models.CharField(
		"Location name",
		max_length=255
	)
	longitude = models.DecimalField(
		"Longitude of Centroid",
		max_digits=10,
		decimal_places=7,
		null=True,
		blank=True
	)
	latitude = models.DecimalField(
		"Latitude of Centroid",
		max_digits=10,
		decimal_places=7,
		null=True,
		blank=True
	)
	
	child_of = models.ForeignKey(
		'self',
		null=True,
		on_delete=models.CASCADE,
		related_name='parent_of'
	)
	
	location_type = models.ForeignKey(
		'LocationType',
		verbose_name="Location Type",
		null=True,
		on_delete=models.CASCADE,
		related_name='type_location'
	)
	
	spatial_extent = models.ForeignKey(
		'Polygon',
		verbose_name="Polygon",
		null=True,
		on_delete=models.CASCADE
	)
	
	uid = models.OneToOneField(
		GeoUid,
		null=False,
		blank=False,
		on_delete=models.CASCADE,
		related_name='uid_place'
	)

	class Meta:
		verbose_name = "Geographic Location"
		verbose_name_plural = "Geographic Locations"
