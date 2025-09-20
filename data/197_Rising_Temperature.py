import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    transform_df1 : pd.DataFrame = (
        weather
            .sort_values(by = ['recordDate'], axis = 0, ascending = True, kind = 'stable')
    )
    transform_df2 : pd.DataFrame =(
        transform_df1
            .assign(
                prev_temp = (
                    transform_df1
                        .loc[:, ['temperature']]
                        .shift(periods = 1, axis = 0))
                , prev_date = (
                    transform_df1
                        .loc[:, ['recordDate']]
                        .shift(periods = 1, axis = 0))
                , last_date = (
                    transform_df1.loc[:, ['recordDate']]- pd.Timedelta(days=1)))
    )

    result_df : pd.DataFrame = (
        transform_df2
            .loc[
                (transform_df2['temperature'] > transform_df2['prev_temp']) & (transform_df2['prev_date'] == transform_df2['last_date'])
                , ['id']]
            .rename(mapper = {'id': 'Id'}, axis = 1)
    )
    return result_df