import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    transform : pd.DataFrame = (
        logs
            .assign(
                prev_num = (
                    logs
                        .loc[:, ['num']]
                        .shift(
                            periods = 1
                            , axis = 0
                        )
                )
                , after_num = (
                    logs
                        .loc[:, ['num']]
                        .shift(
                            periods = -1
                            , axis = 0
                        )                   
                )
            )
    )
    result : pd.DataFrame = (
        transform
            .loc[
                (transform['num'] == transform['prev_num']) & (transform['num'] == transform['after_num'])
                , ['num']
            ]
            .drop_duplicates(
                subset = ['num']
                , keep = 'first'
            )
            .rename(
                mapper = {
                    'num': 'ConsecutiveNums'
                }
                , axis = 1
            )
    )

    return result