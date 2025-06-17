import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    result_df : pd.DataFrame = (
        scores
            .assign(
                rank = (
                    scores
                        .loc[:, ['score']]
                        .rank(
                            axis = 0
                            , method = 'dense'
                            , ascending = False 
                        )
                )
            )
            .sort_values(
                by = ['rank']
                , axis = 0
                , ascending = True
                , kind = 'stable'
            )
            .loc[:, ['score', 'rank']]
    )
    return result_df

