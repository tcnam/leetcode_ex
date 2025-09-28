import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    tran_df : pd.DataFrame = (
        orders
            .groupby(by = ['customer_number'], axis = 0, as_index = False)
            .agg(
                num_order = pd.NamedAgg(column = 'order_number', aggfunc = 'count'))
    )
    result_df : pd.DataFrame = (
        tran_df
            .loc[
                tran_df['num_order'] == tran_df['num_order'].max()
                , ['customer_number']]
    )
    return result_df