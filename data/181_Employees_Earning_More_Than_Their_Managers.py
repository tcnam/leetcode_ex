import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merge_df : pd.DataFrame = (
        employee
            .merge(
                right = employee
                , how = 'left'
                , left_on = ['managerId']
                , right_on = ['id']
                , copy = True
                , suffixes = ['_e', '_m'])
    )

    result_df : pd.DataFrame = (
        merge_df
            .loc[
                merge_df['salary_e'] > merge_df['salary_m']
                , ['name_e']]
            .rename(
                mapper = {
                    'name_e': 'Employee'
                }
                , axis = 1)
    )
    return result_df