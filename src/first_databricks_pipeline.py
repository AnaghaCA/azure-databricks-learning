from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F


# Reusable transformation function
def calculate_revenue_with_tax(df: DataFrame) -> DataFrame:
    return df.withColumn(
        "revenue_with_tax",
        F.round(F.col("revenue") * 1.21, 2)
    )


def main():
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("AzureDatabricksLearning")
        .getOrCreate()
    )

    try:
        data = [
            ("Amsterdam", 120),
            ("Rotterdam", 85),
            ("Utrecht", 150)
        ]

        df = spark.createDataFrame(
            data,
            ["city", "revenue"]
        )

        # Call our reusable function
        result = calculate_revenue_with_tax(df)

        print("Sales data after transformation:")
        result.show()

    finally:
        spark.stop()


if __name__ == "__main__":
    main()