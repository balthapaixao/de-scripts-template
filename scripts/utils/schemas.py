import datetime
from dataclasses import dataclass
import pandas as pd
import logging

logger = logging.getLogger(__name__)


@dataclass
class ExampleSchema:
    """Schema for the Example table"""

    id: int
    name: str
    date: datetime.date
    value: float
    quantity: int
    timestamp: datetime.datetime
    checked: bool


class ExampleTable:
    """Example Table"""

    # To be tested

    def __init__(self, table_name: str, schema: ExampleSchema):
        self.schema = schema
        self.table_name = table_name

    def get_schema(self) -> ExampleSchema:
        return self.schema

    def get_table_name(self) -> str:
        return self.table_name

    def convert_date(self, series: pd.Series) -> pd.Series:
        """Convert date to datetime.date"""
        series = pd.to_datetime(series).dt.date
        return series

    def convert_timestamp(self, series: pd.Series) -> pd.Series:
        """Convert timestamp to datetime.datetime"""
        series = pd.to_datetime(series)
        return series

    def convert_boolean(self, series: pd.Series) -> pd.Series:
        """Convert boolean to bool"""
        series = series.astype(bool)
        return series

    def convert_integer(self, series: pd.Series) -> pd.Series:
        """Convert integer to int"""
        series = series.astype(int)
        return series

    def convert_float(self, series: pd.Series) -> pd.Series:
        """Convert float to float"""
        series = series.astype(float)
        return series

    def convert_string(self, series: pd.Series) -> pd.Series:
        """Convert string to str"""
        series = series.astype(str)
        return series

    def convert(self, series: pd.Series) -> pd.Series:
        """Convert data types"""
        expected_type = self.schema.__annotations__[series.name]
        if expected_type == datetime.date:
            return self.convert_date(series, series.name)
        elif expected_type == datetime.datetime:
            return self.convert_timestamp(series, series.name)
        elif expected_type == bool:
            return self.convert_boolean(series, series.name)
        elif expected_type == int:
            return self.convert_integer(series, series.name)
        elif expected_type == float:
            return self.convert_float(series, series.name)
        elif expected_type == str:
            return self.convert_string(series, series.name)
        else:
            logger.error(f"Data type {expected_type} not supported")
        return series

    def force_data_type(self, series: pd.Series) -> pd.Series:
        """Force data type to schema data type"""
        expected_type = self.schema.__annotations__[series.name]
        try:
            return self.convert(series, expected_type)
        except ValueError as e:
            raise ValueError(
                f"Column {series.name} cannot be converted to {expected_type}"
            ) from e

    def force_data_types(self, data: pd.DataFrame) -> pd.DataFrame:
        """Force data types to schema data types"""
        for column in data.columns:
            data[column] = self.force_data_type(data[column])
        return data
