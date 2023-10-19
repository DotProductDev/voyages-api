Enslaver_options={'id': {'type': 'integer', 'many': False}, 'principal_location__geo_location__id': {'type': 'integer', 'many': False}, 'principal_location__geo_location__uuid': {'type': 'number', 'many': False}, 'principal_location__geo_location__name': {'type': 'string', 'many': False}, 'principal_location__geo_location__longitude': {'type': 'number', 'many': False}, 'principal_location__geo_location__latitude': {'type': 'number', 'many': False}, 'principal_location__geo_location__value': {'type': 'integer', 'many': False}, 'principal_location__geo_location__child_of': {'type': 'integer', 'many': False}, 'principal_location__geo_location__location_type': {'type': 'integer', 'many': False}, 'principal_location__geo_location__spatial_extent': {'type': 'integer', 'many': False}, 'enslaver_zotero_connections__id': {'type': 'integer', 'many': True}, 'enslaver_zotero_connections__zotero_source__id': {'type': 'integer', 'many': True}, 'enslaver_zotero_connections__zotero_source__page_connection__id': {'type': 'integer', 'many': True}, 'enslaver_zotero_connections__zotero_source__page_connection__source_page__id': {'type': 'integer', 'many': True}, 'enslaver_zotero_connections__zotero_source__page_connection__source_page__page_url': {'type': 'number', 'many': True}, 'enslaver_zotero_connections__zotero_source__page_connection__source_page__iiif_manifest_url': {'type': 'number', 'many': True}, 'enslaver_zotero_connections__zotero_source__page_connection__source_page__iiif_baseimage_url': {'type': 'number', 'many': True}, 'enslaver_zotero_connections__zotero_source__page_connection__source_page__image_filename': {'type': 'string', 'many': True}, 'enslaver_zotero_connections__zotero_source__page_connection__source_page__last_updated': {'type': 'number', 'many': True}, 'enslaver_zotero_connections__zotero_source__page_connection__source_page__human_reviewed': {'type': 'boolean', 'many': True}, 'enslaver_zotero_connections__zotero_source__page_connection__zotero_source': {'type': 'integer', 'many': True}, 'enslaver_zotero_connections__zotero_source__item_url': {'type': 'number', 'many': True}, 'enslaver_zotero_connections__zotero_source__zotero_url': {'type': 'number', 'many': True}, 'enslaver_zotero_connections__zotero_source__short_ref': {'type': 'string', 'many': True}, 'enslaver_zotero_connections__zotero_source__zotero_title': {'type': 'string', 'many': True}, 'enslaver_zotero_connections__zotero_source__zotero_date': {'type': 'string', 'many': True}, 'enslaver_zotero_connections__zotero_source__is_legacy_source': {'type': 'boolean', 'many': True}, 'enslaver_zotero_connections__zotero_source__last_updated': {'type': 'number', 'many': True}, 'enslaver_zotero_connections__zotero_source__human_reviewed': {'type': 'boolean', 'many': True}, 'enslaver_zotero_connections__zotero_source__notes': {'type': 'string', 'many': True}, 'enslaver_zotero_connections__zotero_source__legacy_source': {'type': 'integer', 'many': True}, 'enslaver_zotero_connections__page_range': {'type': 'string', 'many': True}, 'enslaver_zotero_connections__enslaver': {'type': 'integer', 'many': True}, 'aliases__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__enslaved_in_relation__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__enslaved_in_relation__enslaved__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__enslaved_in_relation__enslaved__documented_name': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__enslaved_in_relation__relation': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__relation_type__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__relation_type__name': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__place__geo_location__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__place__geo_location__uuid': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__place__geo_location__name': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__place__geo_location__longitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__place__geo_location__latitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__place__geo_location__value': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__place__geo_location__child_of': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__place__geo_location__location_type': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__place__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__dataset': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__uuid': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__name': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__longitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__latitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__value': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__child_of': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__location_type': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__uuid': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__name': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__longitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__latitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__value': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__child_of': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__location_type': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__uuid': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__name': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__longitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__latitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__value': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__child_of': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__location_type': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__uuid': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__name': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__longitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__latitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__value': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__child_of': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__location_type': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__uuid': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__name': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__longitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__latitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__value': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__child_of': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__location_type': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__uuid': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__name': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__longitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__latitude': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__value': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__child_of': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__location_type': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_dates__imp_arrival_at_port_of_dis_sparsedate__day': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_dates__imp_arrival_at_port_of_dis_sparsedate__month': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_dates__imp_arrival_at_port_of_dis_sparsedate__year': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_ship__ship_name': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_name_outcome__particular_outcome__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_name_outcome__particular_outcome__name': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__voyage__voyage_name_outcome__particular_outcome__value': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__relation__date': {'type': 'string', 'many': True}, 'aliases__enslaver_relations__relation__amount': {'type': 'number', 'many': True}, 'aliases__enslaver_relations__relation__is_from_voyages': {'type': 'boolean', 'many': True}, 'aliases__enslaver_relations__relation__source': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__role__id': {'type': 'integer', 'many': True}, 'aliases__enslaver_relations__role__name': {'type': 'string', 'many': True}, 'aliases__alias': {'type': 'string', 'many': True}, 'aliases__manual_id': {'type': 'string', 'many': True}, 'aliases__last_updated': {'type': 'number', 'many': True}, 'aliases__human_reviewed': {'type': 'boolean', 'many': True}, 'aliases__identity': {'type': 'integer', 'many': True}, 'birth_place__geo_location__id': {'type': 'integer', 'many': False}, 'birth_place__geo_location__uuid': {'type': 'number', 'many': False}, 'birth_place__geo_location__name': {'type': 'string', 'many': False}, 'birth_place__geo_location__longitude': {'type': 'number', 'many': False}, 'birth_place__geo_location__latitude': {'type': 'number', 'many': False}, 'birth_place__geo_location__value': {'type': 'integer', 'many': False}, 'birth_place__geo_location__child_of': {'type': 'integer', 'many': False}, 'birth_place__geo_location__location_type': {'type': 'integer', 'many': False}, 'birth_place__geo_location__spatial_extent': {'type': 'integer', 'many': False}, 'death_place__geo_location__id': {'type': 'integer', 'many': False}, 'death_place__geo_location__uuid': {'type': 'number', 'many': False}, 'death_place__geo_location__name': {'type': 'string', 'many': False}, 'death_place__geo_location__longitude': {'type': 'number', 'many': False}, 'death_place__geo_location__latitude': {'type': 'number', 'many': False}, 'death_place__geo_location__value': {'type': 'integer', 'many': False}, 'death_place__geo_location__child_of': {'type': 'integer', 'many': False}, 'death_place__geo_location__location_type': {'type': 'integer', 'many': False}, 'death_place__geo_location__spatial_extent': {'type': 'integer', 'many': False}, 'principal_alias': {'type': 'string', 'many': False}, 'birth_year': {'type': 'integer', 'many': False}, 'birth_month': {'type': 'integer', 'many': False}, 'birth_day': {'type': 'integer', 'many': False}, 'death_year': {'type': 'integer', 'many': False}, 'death_month': {'type': 'integer', 'many': False}, 'death_day': {'type': 'integer', 'many': False}, 'father_name': {'type': 'string', 'many': False}, 'father_occupation': {'type': 'string', 'many': False}, 'mother_name': {'type': 'string', 'many': False}, 'probate_date': {'type': 'string', 'many': False}, 'will_value_pounds': {'type': 'string', 'many': False}, 'will_value_dollars': {'type': 'string', 'many': False}, 'will_court': {'type': 'string', 'many': False}, 'notes': {'type': 'string', 'many': False}, 'is_natural_person': {'type': 'boolean', 'many': False}, 'last_updated': {'type': 'number', 'many': False}, 'human_reviewed': {'type': 'boolean', 'many': False}}