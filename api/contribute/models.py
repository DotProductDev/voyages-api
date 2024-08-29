"""
These models should provide the basis for implementing generic data
contributions. The contributions are diff-based and are inspired by software
version control.
"""

from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL
from django.contrib.auth.models import User

class PublicationBatch(models.Model):
    """
    Represent a batch of contributions that are reviewed and published together.
    Editors can assign contributions to a batch and them work on 
    """
    title = models.CharField(unique=True,
                             help_text="The title of the batch, as shown in the Database History")
    comments = models.TextField(help_text="A comment that will show up in the Database History")
    published = models.BooleanField()

class ChangeSetBase(models.Model):
    """
    The collection of fields stored for each ChangeSet
    """
    author = models.ForeignKey(User, db_index=True, on_delete=PROTECT)
    timestamp = models.DateTimeField(db_index=True)
    changeset = models.JSONField()
    comments = models.TextField(help_text="Comments by the author for this ChangeSet")
    title = models.CharField(db_index=True, help_text="The title of the ChangeSet")

    class Meta:
        """This class is just used as base for other ORM models"""
        abstract: True

class Contribution(ChangeSetBase):
    """
    A data contribution entry. The contribution should contain a ChangeSet
    corresponding to 
    """
    class Status(models.IntegerChoices):
        """
        Contribution status.
        """
        WORK_IN_PROGRESS = 0
        SUBMITTED = 1
        ACCEPTED = 2
        REJECTED = 3

    batch = models.ForeignKey(PublicationBatch,
                              null=True,
                              on_delete=SET_NULL,
                              help_text="An optional batch to which the contrib is assigned")
    status = models.IntegerField(choices=Status.choices, db_index=True)

class ContributionMedia(models.Model):
    """
    Some contributions may include supporting evidence in the form of media: an
    audio recording, a scanned documentary source etc.
    """

    class MediaTypes(models.TextChoices):
        """
        The types of media supported by 
        """
        AUDIO = "audio"
        IMAGE = "image"
        DOCUMENT = "document" # e.g. a PDF

    contribution = models.ForeignKey(Contribution, on_delete=CASCADE)
    name = models.CharField()
    media_type = models.CharField(choices=MediaTypes.choices)
    comments = models.TextField()

class ContributionReview(ChangeSetBase):
    """
    Contribution editorial reviews are changesets stacked on top of the source
    user contribution.

    Each review should be treated as an *immutable* entry. Changes can be
    reversed by stacking a review that undoes/fixes any problems. Our model
    allows multiple editors to work on a contribution collaboratively. We
    enforce a linear history throught the stack. 
    """

    class Action(models.IntegerChoices):
        """The actions that can be performed in a Review"""
        MODIFY = 0 # Apply a changeset to the stack of reviews
        ACCEPT = 1 # Accept the contribution with the stacked changeset
        REJECT = 2 # Reject/archive the contribution
        REOPEN = 3 # Reconsider a previous rejection

    contribution = models.ForeignKey(Contribution, on_delete=PROTECT)
    stack_order = models.IntegerField()
    action = models.IntegerField(choices=Action.choices, db_index=True)

    class Meta:
        """Indices that ensure integrity"""
        unique_together = ["contribution", "stack_order"]


class EntityRevision(models.Model):
    """
    Revision tracking for our data entities.
    """
    # Note: we use a loosely typed entity_id with no ForeignKey constraint by
    # *design*. The revision must be able to exist even if the actual entity is
    # no longer present in the table (e.g. it was deleted).
    entity_id = models.CharField()
    entity_type = models.CharField()
    revision_number = models.IntegerField()
    snapshot = models.JSONField()
    changeset = models.JSONField()

    class Meta:
        """Indices that ensure integrity"""
        unique_together = ["entity_id", "entity_type", "revision_number"]
