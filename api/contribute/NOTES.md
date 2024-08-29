# Design of the Contribution feature

Our Contribution feature is designed around flexibility and data integrity.
Entities that enable contributions may also take part in version control with
revisions and snapshots, allowing auditing of historical changes and tracking
every person involved in producing the updated version of the entity.

Some entities may be mostly read-only with eventual changes made through an
admin interface, for instance, Places, enumeration values etc. The contribution
system may propose changes to such entities. For instance, a contribution may
reference a location that is not currently geo-coded.

The workhorses of this feature are the *EntitySchema* and *ChangeSet*
abstractions which we describe in this note.

## EntitySchema

We will use an explicit schema to encode information about what constitutes a
complete Entity, including its relations to other entities. This schema is used
for constructing a **view model** of the full entity. This view model then
enables the creation of UIs for viewing and for proposing structured changes to
the entity itself, its relations, or the related entity. 

WIP: review the notes once the design is finalized and can fulfill our goals.

## ChangeSets

This object represents a collection of changes that can be used to produce a
transactional update to the database. These changes may be as simple as
modifying a single text value in an existing record or as complex as
updating/creating/deleting entities in many to many relationships.

WIP: review the notes once the design is finalized and can fulfill our goals.

### The ChangeSet structure

