from datasets.records.api import DatasetsDraft, DatasetsRecord
from datasets.services.files.schema import DatasetsFileSchema
from datasets.services.records.permissions import DatasetsPermissionPolicy
from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin


class DatasetsFileServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """DatasetsRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/datasets/<pid_value>"

    base_permission_policy_cls = DatasetsPermissionPolicy

    schema = DatasetsFileSchema

    record_cls = DatasetsRecord

    service_id = "datasets_file"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "datasets"
    allow_upload = False

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/datasets/{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/datasets/{id}/files/{key}/commit"),
            "content": FileLink("{+api}/datasets/{id}/files/{key}/content"),
            "preview": FileLink("{+ui}/datasets/files/{key}/preview"),
            "self": FileLink("{+api}/datasets/{id}/files/{key}"),
        }


class DatasetsFileDraftServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    """DatasetsDraft service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/datasets/<pid_value>/draft"

    schema = DatasetsFileSchema

    record_cls = DatasetsDraft

    service_id = "datasets_file_draft"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        DataComponent,
    ]

    model = "datasets"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/datasets/{id}/draft/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/datasets/{id}/draft/files/{key}/commit"),
            "content": FileLink("{+api}/datasets/{id}/draft/files/{key}/content"),
            "self": FileLink("{+api}/datasets/{id}/draft/files/{key}"),
        }
