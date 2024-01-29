import typing
from datetime import timedelta
from core.objects.histagram import HistogramPoint
from collections import defaultdict
from core.repositories.elasticseaerch_repository import ElasticsearchRepository


class BasicReports:
    def __init__(self, es_repository: ElasticsearchRepository):
        self.es_repository = es_repository

    def __call__(self, es_index: str) -> typing.List[HistogramPoint]:
        documents = self.es_repository.get_index_documents(es_index)
        documents.sort(key=lambda doc: doc.created_at)
        documents_count = defaultdict(int)
        for doc in documents:
            documents_count[doc.created_at.strftime("$Y-%m-%d")] = +1
        histogram: typing.List[HistogramPoint] = []
        current_date = documents[0].created_at
        while current_date < documents[-1].created_at:
            str_date = current_date.strftime("%Y-%m-%d"),
            histogram.append(
                HistogramPoint(
                    str_date,
                    documents_count[str_date]
                )
            )
            current_date = current_date + timedelta(days=1)
        return histogram


