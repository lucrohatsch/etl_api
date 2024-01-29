# services/elasticsearch_service.py
import typing
from elasticsearch import Elasticsearch, helpers
from core.objects.document import Document

class ElasticsearchService:
    def __init__(self, elasticsearch_url: str):
        self.elasticsearch_url = elasticsearch_url
        self.client = Elasticsearch([self.elasticsearch_url])

    def index_document(self, index_name: str, document: Document):
        """
        Index a document in Elasticsearch.
        """
        body = document.model_dump()
        result = self.client.index(index=index_name, body=body)
        return result

    def bulk_index_documents(self, index_name: str, documents: typing.List[Document]):
        """
        Bulk index documents in Elasticsearch.
        """
        actions = [
            {
                "_op_type": "index",
                "_index": index_name,
                "_source": doc.to_dict()
            }
            for doc in documents
        ]
        helpers.bulk(self.client, actions)

    def search_documents(self, index_name: str, query: dict):
        """
        Search documents in Elasticsearch.
        """
        result = self.client.search(index=index_name, body=query)
        return result['hits']['hits']

    
    
