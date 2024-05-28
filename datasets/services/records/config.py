from datasets.records.api import DatasetsDraft, DatasetsRecord
from datasets.services.records.permissions import DatasetsPermissionPolicy
from datasets.services.records.results import DatasetsRecordItem, DatasetsRecordList
from datasets.services.records.search import DatasetsSearchOptions
from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_drafts_resources.services.records.config import is_record
from invenio_records_resources.services import (
    ConditionalLink,
    RecordLink,
    pagination_links,
)
from invenio_records_resources.services.records.components import DataComponent
from nr_metadata.data.services.records.schema import NRDataRecordSchema
from oarepo_runtime.records import has_draft, is_published_record
from oarepo_runtime.services.components import OwnersComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent


class DatasetsServiceConfig(
    PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig
):
    """DatasetsRecord service config."""

    result_item_cls = DatasetsRecordItem

    result_list_cls = DatasetsRecordList

    PERMISSIONS_PRESETS = ["communities"]

    url_prefix = "/datasets/"

    base_permission_policy_cls = DatasetsPermissionPolicy

    schema = NRDataRecordSchema

    search = DatasetsSearchOptions

    record_cls = DatasetsRecord

    service_id = "datasets"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordDraftsServiceConfig.components,
        OwnersComponent,
        DraftFilesComponent,
        FilesComponent,
        DataComponent,
    ]

    model = "datasets"
    draft_cls = DatasetsDraft
    search_drafts = DatasetsSearchOptions

    @property
    def links_item(self):
        return {
            "draft": RecordLink("{+api}/datasets/{id}/draft"),
            "edit_html": RecordLink("{+ui}/datasets/{id}/edit", when=has_draft),
            "files": ConditionalLink(
                cond=is_record,
                if_=RecordLink("{+api}/datasets/{id}/files"),
                else_=RecordLink("{+api}/datasets/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/datasets/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/datasets/{id}/latest"),
            "publish": RecordLink("{+api}/datasets/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/datasets/{id}"),
            "requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/datasets/{id}/requests"),
                else_=RecordLink("{+api}/datasets/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/datasets/{id}"),
                else_=RecordLink("{+api}/datasets/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+ui}/datasets/{id}"),
                else_=RecordLink("{+ui}/datasets/{id}/preview"),
            ),
            "versions": RecordLink("{+api}/datasets/{id}/versions"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/datasets/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/datasets/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/datasets/{id}/versions{?args*}"),
        }
