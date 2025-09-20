import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    transform_df : pd.DataFrame = (
        insurance
            .assign(
                valid_tiv_2015 = (
                    insurance.duplicated(
                        subset = ['tiv_2015']
                        , keep = False
                    )))
            .drop_duplicates(
                subset = ['lat', 'lon']
                , keep = False)
    )
    result : pd.DataFrame = (
        transform_df
            .loc[
                (transform_df['valid_tiv_2015'] == True)
                , ['tiv_2016']]
            .sum(axis = 0)
            .round(decimals = 2)
            .to_frame(name = 'tiv_2016')
    )
    return result