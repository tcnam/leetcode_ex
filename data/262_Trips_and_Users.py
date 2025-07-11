import pandas as pd
import numpy as np
import datetime

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    merge_df: pd.DataFrame = (
        trips
            .assign(
                status_flag = (
                    np.select(
                        condlist = [trips['status'] == 'completed']
                        , choicelist = [0]
                        , default = 1)))
            .merge(right = users, how = 'left'
                    , left_on = ['client_id'], right_on = ['users_id']
                    # , suffixes = ['_trip', '_client']
                    , copy = True)
            .merge(right = users, how = 'left'
                    , left_on= ['driver_id'], right_on = ['users_id']
                    , suffixes = ['_client', '_driver']
                    , copy = True)
    )

    transform_df: pd.DataFrame = (
        merge_df
            .loc[
                (merge_df['banned_driver'] == 'No') 
                    & (merge_df['banned_client'] == 'No')
                    & (pd.to_datetime(merge_df['request_at']) >= datetime.datetime.strptime('2013-10-01', '%Y-%m-%d'))
                    & (pd.to_datetime(merge_df['request_at']) <= datetime.datetime.strptime('2013-10-03', '%Y-%m-%d'))
                , ['request_at', 'status_flag']
            ]
            .groupby(by = ['request_at'], axis = 0, as_index = False)
            .agg(
                trip_count = pd.a(column = 'status_flag', aggfunc = 'count')
                , cancel_trip_count = pd.NamedAgg(column = 'status_flag', aggfunc = 'sum')
            )
    )

    result_df: pd.DataFrame = (
        transform_df
            .assign(
                cancel_rate = (
                    (transform_df['cancel_trip_count'] / transform_df['trip_count']).round(decimals = 2))
                )
            .loc[
                :
                , ['request_at', 'cancel_rate']
            ]
            .rename(
                mapper = {
                    'request_at': 'Day'
                    , 'cancel_rate': 'Cancellation Rate'} 
                , axis = 1)
    )


    return result_df