from datasets.files.api import DatasetsFileDraft
from datasets.files.requests.resolvers import DatasetsFileDraftResolver
from datasets.records.api import DatasetsDraft, DatasetsRecord
from datasets.records.requests.delete_record.types import DeleteRecordRequestType
from datasets.records.requests.edit_record.types import EditRecordRequestType
from datasets.records.requests.publish_draft.types import PublishDraftRequestType
from datasets.records.requests.resolvers import DatasetsDraftResolver, DatasetsResolver
from datasets.resources.files.config import (
    DatasetsFileDraftResourceConfig,
    DatasetsFileResourceConfig,
)
from datasets.resources.files.resource import (
    DatasetsFileDraftResource,
    DatasetsFileResource,
)
from datasets.resources.records.config import DatasetsResourceConfig
from datasets.resources.records.resource import DatasetsResource
from datasets.services.files.config import (
    DatasetsFileDraftServiceConfig,
    DatasetsFileServiceConfig,
)
from datasets.services.files.service import (
    DatasetsFileDraftService,
    DatasetsFileService,
)
from datasets.services.records.config import DatasetsServiceConfig
from datasets.services.records.service import DatasetsService
from oarepo_requests.resolvers.ui import (
    FallbackEntityReferenceUIResolver,
    GroupEntityReferenceUIResolver,
    RecordEntityDraftReferenceUIResolver,
    RecordEntityReferenceUIResolver,
    UserEntityReferenceUIResolver,
)
from oarepo_requests.resources.draft.resource import DraftRecordRequestsResource
from oarepo_requests.services.draft.service import DraftRecordRequestsService
from oarepo_runtime.records.entity_resolvers import GroupResolver, UserResolver

DATASETS_RECORD_RESOURCE_CONFIG = DatasetsResourceConfig


DATASETS_RECORD_RESOURCE_CLASS = DatasetsResource


DATASETS_RECORD_SERVICE_CONFIG = DatasetsServiceConfig


DATASETS_RECORD_SERVICE_CLASS = DatasetsService


DATASETS_REQUESTS_RESOURCE_CLASS = DraftRecordRequestsResource


DATASETS_REQUESTS_SERVICE_CLASS = DraftRecordRequestsService


REQUESTS_REGISTERED_TYPES = [
    DeleteRecordRequestType(),
    EditRecordRequestType(),
    PublishDraftRequestType(),
]


REQUESTS_ENTITY_RESOLVERS = [
    UserResolver(),
    GroupResolver(),
    DatasetsResolver(
        record_cls=DatasetsRecord, service_id="datasets", type_key="datasets"
    ),
    DatasetsDraftResolver(
        record_cls=DatasetsDraft, service_id="datasets", type_key="datasets_draft"
    ),
    DatasetsFileDraftResolver(
        record_cls=DatasetsFileDraft,
        service_id="datasets_file_draft",
        type_key="datasets_file_draft",
    ),
]


ENTITY_REFERENCE_UI_RESOLVERS = {
    "user": UserEntityReferenceUIResolver("user"),
    "fallback": FallbackEntityReferenceUIResolver("fallback"),
    "group": GroupEntityReferenceUIResolver("group"),
    "datasets": RecordEntityReferenceUIResolver("datasets"),
    "datasets_draft": RecordEntityDraftReferenceUIResolver("datasets_draft"),
}
REQUESTS_UI_SERIALIZATION_REFERENCED_FIELDS = ["created_by", "receiver", "topic"]


DATASETS_FILES_RESOURCE_CONFIG = DatasetsFileResourceConfig


DATASETS_FILES_RESOURCE_CLASS = DatasetsFileResource


DATASETS_FILES_SERVICE_CONFIG = DatasetsFileServiceConfig


DATASETS_FILES_SERVICE_CLASS = DatasetsFileService


DATASETS_DRAFT_FILES_RESOURCE_CONFIG = DatasetsFileDraftResourceConfig


DATASETS_DRAFT_FILES_RESOURCE_CLASS = DatasetsFileDraftResource


DATASETS_DRAFT_FILES_SERVICE_CONFIG = DatasetsFileDraftServiceConfig


DATASETS_DRAFT_FILES_SERVICE_CLASS = DatasetsFileDraftService
