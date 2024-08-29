// The initial design of the Schema and ChangeSet types together with
// basic functionality will be placed in this file. We will later migrate this
// to the UI project.

export interface ValidationMessage {
    value: any
    message: string
    type: "Suggestion" | "Warning" | "Error"
}

export type PropertyValidation = (value: any) => ValidationMessage[]

export const nonNullValidation: PropertyValidation = (value: any) => {
    if (value === null || value === undefined || value === "") {
        return [{
            value,
            message: "Value must be non-null",
            type: "Error"
        }]
    }
    return []
}

export const lengthValidation = (minLen: number, maxLen: number): PropertyValidation =>
    (value) => {
        if (typeof value !== "string") {
            return [{
                value,
                message: "Expected a 'string' value",
                type: "Error"
            }]
        }
        if (value.length < minLen) {
            return [{
                value,
                message: `Minimum length allowed is ${minLen}.`,
                type: "Error"
            }]
        }
        if (value.length > maxLen) {
            return [{
                value,
                message: `Maximum length allowed is ${minLen}.`,
                type: "Error"
            }]
        }
        return []
    }

export const combineValidations = (...validations: PropertyValidation[]): PropertyValidation =>
    (value: any) => validations.flatMap(v => v(value))

export interface BaseProperty {
    uid: string
    type: string
    label: string
    backingField: string
    description?: string
    /**
     * An optional logical grouping of properties.
     */
    section?: string
    validation?: PropertyValidation
}

export interface TextProperty extends BaseProperty {
    readonly type: "text"
}

const rangeValidation = (minValue: number, maxValue: number): PropertyValidation => (value: any) => {
    if (typeof value !== "number") {
        return [{
            value,
            message: "Expected a number",
            type: "Error"
        }]
    }
    if (value < minValue) {
        return [{
            value,
            message: `Value smaller than ${minValue}`,
            type: "Error"
        }]
    }
    if (value > maxValue) {
        return [{
            value,
            message: `Value larger than ${maxValue}`,
            type: "Error"
        }]
    }
    return []
}

export interface NumberProperty extends BaseProperty {
    readonly type: "number"
}

export interface PartialDate {
    year: number
    month?: number
    day?: number
}

const isPartialDate = (value: any): value is PartialDate => value && value.year;

export const dateValidation = (allowPartial: boolean): PropertyValidation => (value: any) => {
    if (!isPartialDate(value)) {
        return [{
            value,
            message: `Expected a ${allowPartial ? 'partial ' : ''} date`,
            type: "Error"
        }]
    }
    if (!allowPartial && !value.month && !value.day) {
        return [{
            value,
            message: "The month and day values are required",
            type: "Error"
        }]
    }
    if (!value.month && value.day) {
        return [{
            value,
            message: "The month value is required if a day is specified",
            type: "Error"
        }]
    }
    // Check if the date is valid, e.g. 2024-02-30 should fail validation.
    const date = new Date(`${value.year}-${value.month ?? 1}-${value.day ?? 1}`)
    const valid = date instanceof Date && !isNaN(date.getDate())
    return valid ? [] : [{
        value,
        message: "The date does not exist",
        type: "Error"
    }]
}

export interface DateProperty extends BaseProperty {
    readonly type: "date"
}

export interface EntityLinkBaseProperty extends BaseProperty {
    entityType: string
    /**
     * If set to true, the inner entity can only be selected, but not changed.
     */
    isInnerEntityReadonly: boolean
}

export interface EntityValueProperty extends EntityLinkBaseProperty {
    readonly type: "entityValue"
    /**
     * - ManyToOne: the foreign key to the entity is placed in the outer
     *   (parent) entity at the backingField.
     * - OneToOne: the inner (linked) entity has a FK to the outer entity in the
     *   backingField.  
     */
    linkMode: "ManyToOne" | "OneToOne"
}

export interface EntityListProperty extends EntityLinkBaseProperty {
    readonly type: "entityList"
    /**
     * The model that backs this many-to-many relationship.
     */
    backingModel: string
    entityType: string
}

export interface TableProperty extends Omit<BaseProperty, "backingField"> {
    readonly type: "table"
    columns: string[]
    rows: string[]
    cellField: (col: number, row: number) => string
}

export type Property = TextProperty | NumberProperty | EntityValueProperty | 
    EntityListProperty | TableProperty

export type EntityContributionMode = "Full" | "Owned" | "ReadOnly" 

export interface EntitySchema {
    name: string
    backingModel: string
    contributionMode: EntityContributionMode
    properties: Property[]
}

const NationalitySchema: EntitySchema = {
    name: "Nationality",
    backingModel: "nationality",
    contributionMode: "ReadOnly",
    properties: [{
        uid: "nationality_name",
        type: "text",
        label: "Nation name",
        backingField: "name",
        description: "Name of the nation"
    }, {
        uid: "nationality_code",
        type: "number",
        label: "Code",
        backingField: "value",
        description: "Identification code for the Nation"
    }]
}

const VesselEntitySchema: EntitySchema = {
    name: "Vessel",
    backingModel: "voyageship",
    contributionMode: "Owned",
    properties: [{
        uid: "vessel_name",
        type: "text",
        label: "Name of vessel",
        backingField: "ship_name",
        description: "The name of the ship",
        validation: lengthValidation(3, 255)
    }, {
        uid: "vessel_carrier",
        type: "entityValue",
        label: "National carrier",
        backingField: "nationality_ship",
        linkMode: "ManyToOne",
        entityType: "Nationality",
        isInnerEntityReadonly: true
    }, {
        uid: "vessel_tonnage",
        type: "number",
        label: "Tonnage of vessel",
        backingField: "tonnage"        
    }]
}

const VoyageItinerarySchema: EntitySchema = {
    name: "VoyageItinerary",
    backingModel: "voyageitinerary",
    contributionMode: "Owned",
    properties: [{
        uid: "itinerary_port_of_departure",
        type: "entityValue",
        entityType: "Location",
        label: "Port of departure",
        backingField: "port_of_departure",
        linkMode: "ManyToOne",
        isInnerEntityReadonly: true
    }]
}

const SectionSNO = "Ship, Nations, Owners"
const SectionNumbers = "Slaves (numbers)"
const SectionCharacteristics = "Slaves (Characteristics)"

const VoyageSlaveNumbersSchema: EntitySchema = {
    name: "Voyage Slave Numbers",
    backingModel: "voyageslavenumbers",
    contributionMode: "Owned",
    properties: [{
        uid: "sn_num_slaves_intended_first_port",
        type: "number",
        label: "Slaves intended from first port of purchase",
        backingField: "num_slaves_intended_first_port",
        section: SectionNumbers
    }, {
        type: "table",
        uid: "sn_characteristics",
        label: "Slave characteristics",
        section: SectionCharacteristics,
        columns: ['MEN', 'WOMEN', 'BOY', 'GIRL', 'MALE', 'FEMALE', 'ADULT', 'CHILD', 'INFANT'],
        rows: [
            "Embarked slaves (first port)",
            "Embarked slaves (second port)",
            "Embarked slaves (third port)",
            "Died on voyage",
            "Disembarked slaves (first port)",
            "Disembarked slaves (second port)"
        ],
        cellField: (col, row) => `TODO ${col}x${row}`
    }]
}

const VoyageEntitySchema: EntitySchema = {
    name: "Voyage",
    backingModel: "voyage",
    contributionMode: "Full",
    properties: [{
        type: "number",
        uid: "voyage_id",
        label: "Voyage ID",
        backingField: "voyage_id",
        description: "The unique ID of the voyage",
        validation: rangeValidation(1, 99999999999)
    }, {
        type: "entityValue",
        uid: "voyage_vessel",
        linkMode: "OneToOne",
        backingField: "voyage",
        entityType: "Vessel",
        label: "Ship",
        description: "Ship that performed the voyage",
        section: SectionSNO,
        isInnerEntityReadonly: false
    }, {
        type: "entityValue",
        uid: "voyage_numbers",
        linkMode: "OneToOne",
        backingField: "voyage",
        entityType: "Voyage Slave Numbers",
        label: "",
        section: SectionNumbers,
        isInnerEntityReadonly: false
    }]
}

export const AllSchemas = [
    NationalitySchema,
    VesselEntitySchema,
    VoyageItinerarySchema,
    VoyageSlaveNumbersSchema,
    VoyageEntitySchema
]

// PART II: ChangeSets

export interface DirectPropertyChange {
    property: Pick<TextProperty | NumberProperty | DateProperty, "type" | "uid">
    current: any
    changed: any
    comments: string
}

export interface NewEntityRef {
    type: "newEntityRef"
    tempId: string
}

export interface LinkedEntitySelectionChange {
    property: Pick<EntityValueProperty, "type" | "uid">
    /**
     * The id of the current selected entity.
     */
    current: string | null
    /**
     * The id of the selected entity in the change.
     */
    next: string | NewEntityRef | null
    comments: string
}

export interface OwnedEntityChange {
    property: Pick<EntityValueProperty, "type" | "uid">
    ownedEntityId: string | NewEntityRef
    changes: PropertyChange[]
    comments: string
}

export interface EntityListChange {
    property: Pick<EntityListProperty, "type" | "uid">
    /**
     * Ids removed from the list.
     */
    removed: string[]
    /**
     * Ids of existing or entities created in the same changeset to be added to
     * the list.
     */
    added: (string | NewEntityRef)[]
    modified: OwnedEntityChange[]
    comments: string
}

export type PropertyChange = DirectPropertyChange | LinkedEntitySelectionChange | 
    OwnedEntityChange | EntityListChange

export interface EntityUpdate {
    readonly type: "update"
    schema: string
    entityId: string
    changes: PropertyChange[]
}

export interface EntityDeletion {
    readonly type: "deletion"
    schema: string
    entityId: string
}

export interface EntityCreation {
    readonly type: "creation"
    schema: string
    ref: NewEntityRef
}

export type EntityChange = EntityCreation | EntityUpdate | EntityDeletion

export interface ChangeSet {
    title: string
    comments: string
    entityChanges: EntityChange[]
}