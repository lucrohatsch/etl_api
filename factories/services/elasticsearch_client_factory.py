from services.elasticsearch_service import ElasticsearchService
from api.config.secrets import ELASTIC_URL, ELASTIC_PSW, ELASTIC_USR


def get_elasticsearch_client():
    return ElasticsearchService(
        elasticsearch_url=ELASTIC_URL
    )
