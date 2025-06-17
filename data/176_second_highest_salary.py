import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    transform_df : pd.DataFrame = (
        employee
            .drop_duplicates(
                subset = ['salary']
                , keep = 'first'
            )
            .assign(
                # create new column call rank using denserank parition no order by salary desc
                rank = (
                    employee
                        .loc[:, ['salary']]
                        .rank(
                            axis = 0
                            , method = 'dense'
                            , ascending = False
                        )
                )
            )
    )
    result_df : pd.DataFrame = (
        transform_df
            .loc[
                transform_df['rank'] == 2
                , ['salary']
            ]
            .rename(
                mapper = {
                    'salary': 'SecondHighestSalary'
                }
                ,axis = 1
            )
    )

    # result_df : pd.DataFrame = (
    #     employee
    #         .drop_duplicates(
    #             subset = ['salary']
    #             , keep = 'first'
    #         )
    #         .sort_values(
    #             by = ['salary']
    #             , axis = 0
    #             , ascending = False
    #             , kind = 'stable'
    #         )
    #         .rename(
    #             mapper = {
    #                 'salary': 'SecondHighestSalary'
    #             }
    #             ,axis = 1
    #         )
    # )

    if len(result_df) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    return result_df
