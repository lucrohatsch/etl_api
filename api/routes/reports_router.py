from fastapi import APIRouter, HTTPException, Depends
from core.repositories.elasticseaerch_repository import ElasticsearchRepository
from factories.repositories.elasticsearch_repository_factory import get_elasticsearch_repository
from api.dtos.basic_reports_dto import BasicReportsPayload, BasicReportsResponse
from core.use_cases.basic_reports_case import BasicReports

reports_router = APIRouter()


@reports_router.get("/basics", response_class=BasicReportsResponse)
async def get_basic_reports(payload: BasicReportsPayload, es_repository: ElasticsearchRepository = Depends(get_elasticsearch_repository)):
    report_use_case = BasicReports(es_repository)
    return report_use_case(payload.es_index)
