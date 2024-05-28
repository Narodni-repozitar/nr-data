from invenio_db import db
from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from sqlalchemy_utils import UUIDType


class DatasetsParentMetadata(db.Model, RecordMetadataBase):

    __tablename__ = "datasets_parent_record_metadata"


class DatasetsMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for DatasetsRecord metadata."""

    __tablename__ = "datasets_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = DatasetsParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class DatasetsDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for DatasetsDraft metadata."""

    __tablename__ = "datasets_draft_metadata"

    __parent_record_model__ = DatasetsParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class DatasetsParentState(db.Model, ParentRecordStateMixin):
    table_name = "datasets_parent_state_metadata"

    __parent_record_model__ = DatasetsParentMetadata
    __record_model__ = DatasetsMetadata
    __draft_model__ = DatasetsDraftMetadata
