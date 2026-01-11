from src.app.config import settings
from src.app.schemas.benchmark import BenchmarkAverageStats, BenchmarkResult
from src.app.tests.fixtures.load_fixtures import load_test_benchmarks


async def load_benchmark_results() -> list[BenchmarkResult]:
    if settings.DEBUG:
        # DEBUG mode allows us to get data directly from the test_database.json file which mimics the database
        return await load_test_benchmarks()

    raise NotImplementedError('Live mode is not implemented yet.')


async def calculate_average_stats(results: list) -> BenchmarkAverageStats:
    if not results:
        return BenchmarkAverageStats(
            avg_token_count=0.0,
            avg_time_to_first_token=0.0,
            avg_time_per_output_token=0.0,
            avg_total_generation_time=0.0,
        )

    def avg(field: str) -> float:
        return round(sum(getattr(r, field) for r in results) / len(results), 2)

    return BenchmarkAverageStats(
        avg_token_count=avg('token_count'),
        avg_time_to_first_token=avg('time_to_first_token'),
        avg_time_per_output_token=avg('time_per_output_token'),
        avg_total_generation_time=avg('total_generation_time'),
    )
