import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result: pd.DataFrame = (
        activity
            .groupby(by = ['player_id'], axis = 0, as_index = False)
            .agg(
                first_login = pd.NamedAgg(column = 'event_date', aggfunc = 'min'))
            .drop_duplicates(
                subset = ['player_id', 'first_login']
                , keep = 'first')
    )
    return result