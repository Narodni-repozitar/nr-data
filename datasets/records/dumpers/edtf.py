from oarepo_runtime.records.dumpers.edtf_interval import EDTFIntervalDumperExt


class DatasetsEDTFIntervalDumperExt(EDTFIntervalDumperExt):
    """edtf interval dumper."""

    paths = [
        "metadata/dateCollected",
        "metadata/dateCreated",
        "metadata/events/eventDate",
    ]


class DatasetsDraftEDTFIntervalDumperExt(EDTFIntervalDumperExt):
    """edtf interval dumper."""

    paths = [
        "metadata/dateCollected",
        "metadata/dateCreated",
        "metadata/events/eventDate",
    ]
