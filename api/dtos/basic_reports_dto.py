import typing
from datetime import datetime
from pydantic import BaseModel
from core.objects.document import Document
from core.objects.histagram import HistogramPoint

class BasicReportsPayload:
    es_index: str
    since_iso_time: datetime
    to_iso_time: datetime


class BasicReportsResponse:
    histogram: typing.List[HistogramPoint]
    data: typing.List[Document]
    errors: typing.List
