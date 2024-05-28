from datasets.services.files.config import DatasetsFileServiceConfig


class DatasetsFilePublishedServiceConfig(DatasetsFileServiceConfig):
    service_id = "published_datasets_file"

    @property
    def components(self):
        return [*super().components]
