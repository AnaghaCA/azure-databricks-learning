import pytest
from pyspark.sql import SparkSession

from src.first_databricks_pipeline import calculate_revenue_with_tax


@pytest.fixture
def spark():
    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("revenue-tax-test")
        .getOrCreate()
    )

    try:
        yield spark
    finally:
        spark.stop()


def test_calculate_revenue_with_tax(spark):
    df = spark.createDataFrame(
        [("Amsterdam", 100.0), ("Rotterdam", 200.0)],
        ["city", "revenue"],
    )

    result = calculate_revenue_with_tax(df)

    actual_values = [
        round(row["revenue_with_tax"], 2)
        for row in result.orderBy("city").collect()
    ]

    assert actual_values == [121.0, 242.0]
