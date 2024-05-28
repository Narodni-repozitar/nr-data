from oarepo_requests.services.results import RequestsComponent, RequestTypesComponent
from oarepo_runtime.services.results import RecordItem, RecordList


class DatasetsRecordItem(RecordItem):
    """DatasetsRecord record item."""

    components = [*RecordItem.components, RequestsComponent(), RequestTypesComponent()]


class DatasetsRecordList(RecordList):
    """DatasetsRecord record list."""

    components = [*RecordList.components]
