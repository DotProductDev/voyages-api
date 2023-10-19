Enslaved_options={'id': {'type': 'integer', 'many': False}, 'post_disembark_location__geo_location__id': {'type': 'integer', 'many': False}, 'post_disembark_location__geo_location__uuid': {'type': 'number', 'many': False}, 'post_disembark_location__geo_location__name': {'type': 'string', 'many': False}, 'post_disembark_location__geo_location__longitude': {'type': 'number', 'many': False}, 'post_disembark_location__geo_location__latitude': {'type': 'number', 'many': False}, 'post_disembark_location__geo_location__value': {'type': 'integer', 'many': False}, 'post_disembark_location__geo_location__child_of': {'type': 'integer', 'many': False}, 'post_disembark_location__geo_location__location_type': {'type': 'integer', 'many': False}, 'post_disembark_location__geo_location__spatial_extent': {'type': 'integer', 'many': False}, 'captive_fate__id': {'type': 'integer', 'many': False}, 'captive_fate__name': {'type': 'string', 'many': False}, 'enslaved_relations__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_type__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_type__name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__principal_alias': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__birth_year': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__birth_month': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__birth_day': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__death_year': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__death_month': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__death_day': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__father_name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__father_occupation': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__mother_name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__probate_date': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__will_value_pounds': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__will_value_dollars': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__will_court': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__notes': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__is_natural_person': {'type': 'boolean', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__last_updated': {'type': 'number', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__human_reviewed': {'type': 'boolean', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__birth_place': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__death_place': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__identity__principal_location': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__alias': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__manual_id': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__last_updated': {'type': 'number', 'many': True}, 'enslaved_relations__relation__relation_enslavers__enslaver_alias__human_reviewed': {'type': 'boolean', 'many': True}, 'enslaved_relations__relation__relation_enslavers__role__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__relation_enslavers__role__name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__relation_enslavers__relation': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__dataset': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__uuid': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__longitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__latitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__value': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__child_of': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__location_type': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_port_voyage_begin__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__uuid': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__longitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__latitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__value': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__child_of': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__location_type': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_place_of_slave_purchase__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__uuid': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__longitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__latitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__value': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__child_of': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__location_type': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_port_slave_dis__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__uuid': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__longitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__latitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__value': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__child_of': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__location_type': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_of_slave_purchase__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__uuid': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__longitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__latitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__value': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__child_of': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__location_type': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__imp_principal_region_slave_dis__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__uuid': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__longitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__latitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__value': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__child_of': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__location_type': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_itinerary__int_first_port_dis__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_dates__imp_arrival_at_port_of_dis_sparsedate__day': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_dates__imp_arrival_at_port_of_dis_sparsedate__month': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_dates__imp_arrival_at_port_of_dis_sparsedate__year': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_ship__ship_name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__voyage__voyage_name_outcome__particular_outcome__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__voyage__voyage_name_outcome__particular_outcome__name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__voyage__voyage_name_outcome__particular_outcome__value': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__place__geo_location__id': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__place__geo_location__uuid': {'type': 'number', 'many': True}, 'enslaved_relations__relation__place__geo_location__name': {'type': 'string', 'many': True}, 'enslaved_relations__relation__place__geo_location__longitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__place__geo_location__latitude': {'type': 'number', 'many': True}, 'enslaved_relations__relation__place__geo_location__value': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__place__geo_location__child_of': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__place__geo_location__location_type': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__place__geo_location__spatial_extent': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__date': {'type': 'string', 'many': True}, 'enslaved_relations__relation__amount': {'type': 'number', 'many': True}, 'enslaved_relations__relation__unnamed_enslaved_count': {'type': 'integer', 'many': True}, 'enslaved_relations__relation__text_ref': {'type': 'string', 'many': True}, 'enslaved_relations__relation__is_from_voyages': {'type': 'boolean', 'many': True}, 'enslaved_relations__relation__source': {'type': 'integer', 'many': True}, 'enslaved_relations__enslaved': {'type': 'integer', 'many': True}, 'captive_status__id': {'type': 'integer', 'many': False}, 'captive_status__name': {'type': 'string', 'many': False}, 'language_group__id': {'type': 'integer', 'many': False}, 'language_group__name': {'type': 'string', 'many': False}, 'language_group__uuid': {'type': 'number', 'many': False}, 'language_group__longitude': {'type': 'number', 'many': False}, 'language_group__latitude': {'type': 'number', 'many': False}, 'enslaved_zotero_connections__id': {'type': 'integer', 'many': True}, 'enslaved_zotero_connections__zotero_source__id': {'type': 'integer', 'many': True}, 'enslaved_zotero_connections__zotero_source__page_connection__id': {'type': 'integer', 'many': True}, 'enslaved_zotero_connections__zotero_source__page_connection__source_page__id': {'type': 'integer', 'many': True}, 'enslaved_zotero_connections__zotero_source__page_connection__source_page__page_url': {'type': 'number', 'many': True}, 'enslaved_zotero_connections__zotero_source__page_connection__source_page__iiif_manifest_url': {'type': 'number', 'many': True}, 'enslaved_zotero_connections__zotero_source__page_connection__source_page__iiif_baseimage_url': {'type': 'number', 'many': True}, 'enslaved_zotero_connections__zotero_source__page_connection__source_page__image_filename': {'type': 'string', 'many': True}, 'enslaved_zotero_connections__zotero_source__page_connection__source_page__last_updated': {'type': 'number', 'many': True}, 'enslaved_zotero_connections__zotero_source__page_connection__source_page__human_reviewed': {'type': 'boolean', 'many': True}, 'enslaved_zotero_connections__zotero_source__page_connection__zotero_source': {'type': 'integer', 'many': True}, 'enslaved_zotero_connections__zotero_source__item_url': {'type': 'number', 'many': True}, 'enslaved_zotero_connections__zotero_source__zotero_url': {'type': 'number', 'many': True}, 'enslaved_zotero_connections__zotero_source__short_ref': {'type': 'string', 'many': True}, 'enslaved_zotero_connections__zotero_source__zotero_title': {'type': 'string', 'many': True}, 'enslaved_zotero_connections__zotero_source__zotero_date': {'type': 'string', 'many': True}, 'enslaved_zotero_connections__zotero_source__is_legacy_source': {'type': 'boolean', 'many': True}, 'enslaved_zotero_connections__zotero_source__last_updated': {'type': 'number', 'many': True}, 'enslaved_zotero_connections__zotero_source__human_reviewed': {'type': 'boolean', 'many': True}, 'enslaved_zotero_connections__zotero_source__notes': {'type': 'string', 'many': True}, 'enslaved_zotero_connections__zotero_source__legacy_source': {'type': 'integer', 'many': True}, 'enslaved_zotero_connections__page_range': {'type': 'string', 'many': True}, 'enslaved_zotero_connections__enslaved': {'type': 'integer', 'many': True}, 'documented_name': {'type': 'string', 'many': False}, 'name_first': {'type': 'string', 'many': False}, 'name_second': {'type': 'string', 'many': False}, 'name_third': {'type': 'string', 'many': False}, 'modern_name': {'type': 'string', 'many': False}, 'editor_modern_names_certainty': {'type': 'string', 'many': False}, 'age': {'type': 'integer', 'many': False}, 'gender': {'type': 'integer', 'many': False}, 'height': {'type': 'number', 'many': False}, 'skin_color': {'type': 'string', 'many': False}, 'last_known_date': {'type': 'string', 'many': False}, 'dataset': {'type': 'integer', 'many': False}, 'notes': {'type': 'string', 'many': False}, 'last_updated': {'type': 'number', 'many': False}, 'human_reviewed': {'type': 'boolean', 'many': False}, 'register_country': {'type': 'integer', 'many': False}, 'voyage': {'type': 'integer', 'many': False}, 'sources': {'type': 'integer', 'many': False}}