from datetime import datetime

from fastapi import APIRouter, Query

from src.app.repositories.benchmark import BenchmarkRepository
from src.app.schemas.benchmark import BenchmarkAverageStats, BenchmarkResult


router = APIRouter()


@router.get('/', response_model=list[BenchmarkResult])
async def get_all_results() -> list[BenchmarkResult]:
    """Returns all benchmarking results."""
    return await BenchmarkRepository.get_all_results()


@router.get('/results/average', response_model=BenchmarkAverageStats)
async def get_average_results(
    start_time: datetime | None = Query(None, description='The start time for the time window.'),
    end_time: datetime | None = Query(None, description='The end time for the time window.'),
) -> BenchmarkAverageStats:
    """
    Returns the average performance statistics for benchmarking results.
    If a time window is specified, the statistics are calculated for that window.
    """
    return await BenchmarkRepository.get_average_stats(start_time=start_time, end_time=end_time)
