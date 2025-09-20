import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    transform_df : pd.DataFrame = (
        employee
            .drop_duplicates(
                subset = ['salary']
                , keep = 'first')
            .assign(
                rank = (
                    employee
                        .loc[:, ['salary']]
                        .rank(
                            axis = 0
                            , method = 'dense'
                            , ascending = False
                        )))
    )

    result_df : pd.DataFrame = (
        transform_df
            .loc[
                transform_df['rank'] == N
                , ['salary']]
            .rename (
                mapper = {
                    'salary': f'getNthHighestSalary({N})'
                }
                , axis = 1)
    )

    if len(result_df) < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    return result_df