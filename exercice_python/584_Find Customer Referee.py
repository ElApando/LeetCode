""" Find Customer Referee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who 
referred them.
 
Find the names of the customer that are not referred by the customer with id = 2.
Return the result table in any order.
The result format is in the following example.

Example 1:

Input: 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output: 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
"""

import pandas as pd

def find_products(df_customer: pd.DataFrame) -> pd.DataFrame:
    """find_products

    Parameters:
        - df_customer *(dataframe)* - 
    Returns:
        - 
    """
    df_customer = df_customer.loc[df_customer["referee_id"] != 2]
    # print(df_customer.loc[~df_customer["referee_id"].isin([np.nan])])
    # print(df_customer.loc[~df_customer["referee_id"].isin([2])][["name"]])

    return df_customer[["name"]]

df_data = pd.read_csv("refs/584.txt")
print(find_products(df_data))

# Finite Incantatem
