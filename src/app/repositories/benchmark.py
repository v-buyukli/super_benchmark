from datetime import datetime

from fastapi import HTTPException

from src.app.schemas.benchmark import BenchmarkAverageStats, BenchmarkResult
from src.app.services.benchmark import calculate_average_stats, load_benchmark_results


class BenchmarkRepository:
    @staticmethod
    async def _safe_load_results() -> list[BenchmarkResult]:
        try:
            return await load_benchmark_results()
        except NotImplementedError as e:
            raise HTTPException(status_code=501, detail=str(e))

    @staticmethod
    async def get_all_results() -> list[BenchmarkResult]:
        results = await BenchmarkRepository._safe_load_results()
        return results

    @staticmethod
    async def get_average_stats(
        start_time: datetime | None = None,
        end_time: datetime | None = None,
    ) -> BenchmarkAverageStats:
        if (start_time and end_time) and end_time < start_time:
            raise HTTPException(
                status_code=400,
                detail='`end_time` must be greater than or equal to `start_time`.',
            )

        results = await BenchmarkRepository._safe_load_results()

        if start_time:
            results = [r for r in results if r.timestamp >= start_time]
        if end_time:
            results = [r for r in results if r.timestamp <= end_time]

        return await calculate_average_stats(results=results)
