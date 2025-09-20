import pandas as pd
from typing import (
    List
)

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    col_list: List[str] = ['firstName', 'lastName', 'city', 'state']
    result_df: pd.DataFrame = (
        person
            .merge(
                right = address
                , how = 'left'
                , left_on = ['personId']
                , right_on = ['personId']
                , copy = True)
            .loc[:, col_list]
    )
    return result_df