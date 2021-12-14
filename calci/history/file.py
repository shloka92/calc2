from pathlib import Path
import pandas as pd


class FileHandler:
    """This is the FileHandler class"""

    @staticmethod
    def get_path():
        return str(Path(__file__).parent.absolute()) + "/data/results.csv"

    @staticmethod
    def append(num1, num2, operation, result):
        """Some"""
        df_result = pd.read_csv(FileHandler.get_path())
        df_result.loc[len(df_result.index)] = [num1, num2, operation, result]
        df_result = df_result.drop_duplicates()
        df_result.to_csv(FileHandler.get_path(), index=False)

    @staticmethod
    def read():
        """Some"""
        df_result = pd.read_csv(FileHandler.get_path())
        return list(df_result.values.tolist())

    @staticmethod
    def columns():
        """Some"""
        df_result = pd.read_csv(FileHandler.get_path())
        return df_result.columns.values
