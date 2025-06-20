import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merge_df : pd.DataFrame = (
        customers
            .merge(
                right = orders
                , how = 'left'
                , left_on = ['id']
                , right_on = ['customerId']
                , copy = True
                , suffixes= ['_cust', '_order']
            )

    )

    result_df : pd.DataFrame = (
        merge_df
            .loc[
                (merge_df['id_order'].isna() == True)
                , ['name']
            ]
            .rename(
                mapper = {
                    'name': 'Customers'
                }
                , axis = 1
            )

    )
    return result_df