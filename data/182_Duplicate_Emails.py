import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    group_df : pd.DataFrame = (
        person
            .groupby(
                by = ['email']
                , axis = 0
                , as_index = False)
            .agg(
                id_count = pd.NamedAgg(column = 'id', aggfunc = 'count'))
    )

    result_df : pd.DataFrame = (
        group_df
            .loc[
                (group_df['id_count'] > 1)
                , ['email']]
    )
    return result_df