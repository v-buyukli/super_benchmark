from datetime import datetime

from fastapi import APIRouter

from src.app.repositories.benchmark import BenchmarkRepository
from src.app.schemas.benchmark import BenchmarkAverageStats, BenchmarkResult


router = APIRouter()


@router.get('/', response_model=list[BenchmarkResult])
async def get_all_results() -> list[BenchmarkResult]:
    return await BenchmarkRepository.get_all_results()


@router.get('/results/average/', response_model=BenchmarkAverageStats)
@router.get('/results/average/{start_time}/{end_time}', response_model=BenchmarkAverageStats)
async def average_results(
    start_time: datetime | None = None,
    end_time: datetime | None = None,
) -> BenchmarkAverageStats:
    return await BenchmarkRepository.get_average_stats(start_time=start_time, end_time=end_time)
