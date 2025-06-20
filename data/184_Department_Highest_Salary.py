import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merge_df : pd.DataFrame = (
        employee
            .assign(
                rank = (employee
                            .groupby(
                                by = ['departmentId']
                                , axis = 0
                                , as_index = False
                            )
                            ['salary']
                            .rank(
                                axis = 0
                                , method = 'dense'
                                , ascending = False
                            )
                )
            )
            .merge(
                right = department
                , how = 'inner'
                , left_on = ['departmentId']
                , right_on = ['id']
                , copy = True
                , suffixes = ['_emp', '_depart']
            )
    )

    result_df : pd.DataFrame = (
        merge_df
            .loc[
                merge_df['rank'] == 1
                , ['name_depart', 'name_emp', 'salary']
            ]
            .rename (
                mapper = {
                    'name_depart': 'Department'
                    , 'name_emp': 'Employee'
                    , 'salary': 'Salary'
                }
                , axis = 1
            )
    )
    return result_df