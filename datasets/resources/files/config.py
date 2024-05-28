import importlib_metadata
from datasets.resources.files.ui import (
    DatasetsFileDraftUIJSONSerializer,
    DatasetsFileUIJSONSerializer,
)
from flask_resources import ResponseHandler
from invenio_records_resources.resources import FileResourceConfig


class DatasetsFileResourceConfig(FileResourceConfig):
    """DatasetsFile resource config."""

    blueprint_name = "datasets_file"
    url_prefix = "/datasets/<pid_value>"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.datasets.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                DatasetsFileUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }


class DatasetsFileDraftResourceConfig(FileResourceConfig):
    """DatasetsFileDraft resource config."""

    blueprint_name = "datasets_file_draft"
    url_prefix = "/datasets/<pid_value>/draft"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.datasets.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                DatasetsFileDraftUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
