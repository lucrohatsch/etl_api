from core.objects.document import Document
from services.elasticsearch_service import ElasticsearchService
from core.objects.document import Document
import typing

class ElasticsearchRepository:
    def __init__(self, elasticsearch_service: ElasticsearchService):
        self.elasticsearch_service = elasticsearch_service

    def get_index_documents(self, es_index: str) -> typing.List[Document]:
        index_documents = self.elasticsearch_service.search_documents(index_name=es_index, query={"match_all": {}})
        return [
            Document(
                id=document.get("id")
                # TODO complete 
            )
            for document in index_documents
        ]
