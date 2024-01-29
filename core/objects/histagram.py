from pydantic import BaseModel


class HistogramPoint:
    date: str
    value: int
