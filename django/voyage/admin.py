from django.contrib import admin
from voyage.models import *
from past.models import *

# 
# 
class VoyageCrewInline(admin.StackedInline):
	model=VoyageCrew
	max_num=1
	classes = ['collapse']


class VoyageSourcesTypeAdmin(admin.ModelAdmin):
	list_fields=['group_name']

class BroadRegionAdmin(admin.ModelAdmin):
	search_fields=['broad_region']
	list_fields=['broad_region','value']
	ordering = ['value']

class RegionAdmin(admin.ModelAdmin):
	search_fields=['region']
	list_fields=['region','value']
	autocomplete_fields = ('broad_region',)
	ordering = ['value']

class PlaceAdmin(admin.ModelAdmin):
	search_fields=['place']
	list_fields=['place','value']
	autocomplete_fields = ('region',)
	ordering = ['value']


class VoyageDatesInline(admin.StackedInline):
	model = VoyageDates
	autocomplete_fields=[
		'voyage_began',
		'slave_purchase_began',
		'vessel_left_port',
		'first_dis_of_slaves',
		'date_departed_africa',
		'arrival_at_second_place_landing',
		'third_dis_of_slaves',
		'departure_last_place_of_landing',
		'voyage_completed'
	]
	max_num=1
	classes = ['collapse']
	verbose_name_plural="Voyage Dates"
# 
class VoyageSlavesNumbersInline(admin.StackedInline):
	model=VoyageSlavesNumbers
	classes = ['collapse']
	max_num=1

class ParticularOutcomeAdmin(admin.ModelAdmin):
	list_display = ('label','value')
	list_display_links = ('label',)
	model=ParticularOutcome
	search_fields=['label']
	classes = ['collapse']

class SlavesOutcomeAdmin(admin.ModelAdmin):
	list_display = ('label','value')
	list_display_links = ('label',)
	model=SlavesOutcome
	search_fields=['label']
	classes = ['collapse']
	
class VesselCapturedOutcomeAdmin(admin.ModelAdmin):
	list_display = ('label','value')
	list_display_links = ('label',)
	model=VesselCapturedOutcome
	search_fields=['label']
	classes = ['collapse']

class OwnerOutcomeAdmin(admin.ModelAdmin):
	list_display = ('label','value')
	list_display_links = ('label',)
	model=OwnerOutcome
	search_fields=['label']
	classes = ['collapse']

class ResistanceAdmin(admin.ModelAdmin):
	list_display = ('label','value')
	list_display_links = ('label',)
	model=Resistance
	search_fields=['label']
	classes = ['collapse']
# 
# ##Autocomplete won't work on this
# ##Until we update the voyages table to explicitly point at outcomes
# ##Which I'm still unclear about why it wasn't done that way
# ##But the number of selections on the outcome table is small enough
# ##That we don't hit any performance issues here
# ##So it can stay for now
# ##Until I figure out what's going to break when I migrate that.
# ##It is worth saying that I think it's currently broken
# ##Insofar as you can apply more than one outcome entry to each voyage
# ##But it doesn't appear that this has ever been done
# ##which on this admin page results in multiple possible outcome fields being allowed
class VoyageOutcomeInline(admin.StackedInline):
	max_num = 0
	classes = ['collapse']
	model=VoyageOutcome

class NationalityAdmin(admin.ModelAdmin):
	search_fields=['label']
	model=Nationality

class TonTypeAdmin(admin.ModelAdmin):
	search_fields=['label']
	model=TonType

class RigOfVesselAdmin(admin.ModelAdmin):
	model=RigOfVessel
	search_fields=['label']


class VoyageShipInline(admin.StackedInline):
	model = VoyageShip
	max_num = 1
	autocomplete_fields=[
		'nationality_ship',
		'ton_type',
		'rig_of_vessel',
		'vessel_construction_place',
		'vessel_construction_region',
		'registered_place',
		'registered_region',
		'imputed_nationality'
	]
	classes = ['collapse']

class VoyageItineraryInline(admin.StackedInline):
	model = VoyageItinerary
	max_num = 1
	autocomplete_fields=[
		'imp_broad_region_voyage_begin',
		'port_of_departure',
		'int_first_port_emb',
		'int_second_port_emb',
		'int_first_region_purchase_slaves',
		'int_second_region_purchase_slaves',
		'int_first_port_dis',
		'int_second_port_dis',
		'int_first_region_slave_landing',
		'imp_principal_region_slave_dis',
		'int_second_place_region_slave_landing',
		'first_place_slave_purchase',
		'second_place_slave_purchase',
		'third_place_slave_purchase',
		'first_region_slave_emb',
		'second_region_slave_emb',
		'third_region_slave_emb',
		'port_of_call_before_atl_crossing',
		'first_landing_place',
		'second_landing_place',
		'third_landing_place',
		'first_landing_region',
		'second_landing_region',
		'third_landing_region',
		'place_voyage_ended',
		'region_of_return',
		'broad_region_of_return',
		'imp_port_voyage_begin',
		'imp_region_voyage_begin',
		'imp_broad_region_voyage_begin',
		'principal_place_of_slave_purchase',
		'imp_principal_place_of_slave_purchase',
		'imp_principal_region_of_slave_purchase',
		'imp_broad_region_of_slave_purchase',
		'principal_port_of_slave_dis',
		'imp_principal_port_slave_dis',
		'imp_broad_region_slave_dis'
	]
	classes = ['collapse']
# 
class VoyageSourcesConnectionInline(admin.StackedInline):
	model=VoyageSourcesConnection
	autocomplete_fields=['source']
	fields=['source','text_ref']
	classes = ['collapse']
	extra=0
# 
class VoyageSourcesAdmin(admin.ModelAdmin):
	search_fields=['full_ref']
	list_display=['full_ref','short_ref']
	model=VoyageSources

class VoyageOutcomeInline(admin.StackedInline):
	model=VoyageOutcome
	extra=0
	autocomplete_fields=[
		'particular_outcome',
		'resistance',
		'outcome_slaves',
		'vessel_captured_outcome',
		'outcome_owner'
	]
	classes = ['collapse']

class EnslaverAliasConnectionInline(admin.StackedInline):
	model = EnslaverVoyageConnection
	autocomplete_fields=['enslaver_alias',]
	classes = ['collapse']
	extra=0

class VoyageAdmin(admin.ModelAdmin):
	inlines=(
		VoyageDatesInline,
		VoyageItineraryInline,
		VoyageSourcesConnectionInline,
		EnslaverAliasConnectionInline,
		VoyageCrewInline,
		VoyageOutcomeInline,
		VoyageShipInline,
		VoyageSlavesNumbersInline
	)
	fields=['voyage_id','dataset','voyage_groupings','voyage_in_cd_rom']
	list_display=('voyage_id',)
	search_fields=('voyage_id',)
	model=Voyage


admin.site.register(Voyage, VoyageAdmin)
admin.site.register(VoyageDates)
admin.site.register(VoyageSources, VoyageSourcesAdmin)
admin.site.register(BroadRegion,BroadRegionAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Place,PlaceAdmin)
admin.site.register(VoyageSourcesType,VoyageSourcesTypeAdmin)
admin.site.register(ParticularOutcome, ParticularOutcomeAdmin)
admin.site.register(SlavesOutcome, SlavesOutcomeAdmin)
admin.site.register(VesselCapturedOutcome, VesselCapturedOutcomeAdmin)
admin.site.register(OwnerOutcome, OwnerOutcomeAdmin)
admin.site.register(Resistance, ResistanceAdmin)
admin.site.register(Nationality, NationalityAdmin)
admin.site.register(TonType, TonTypeAdmin)
admin.site.register(RigOfVessel, RigOfVesselAdmin)
