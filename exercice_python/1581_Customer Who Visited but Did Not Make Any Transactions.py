""" Customer Who Visited but Did Not Make Any Transactions

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id is the column with unique values for this table.
This table contains information about the customers who visited the mall.
 
Table: Transactions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id is column with unique values for this table.
This table contains information about the transactions made during the visit_id.

Write a solution to find the IDs of the users who visited without making any transactions and the
number of times they made these types of visits.
Return the result table sorted in any order.
The result format is in the following example.

Example 1:

Input: 
Visits
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |
+----------+-------------+
Transactions
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 5        | 200    |
| 12             | 1        | 910    |
| 13             | 2        | 970    |
+----------------+----------+--------+
Output: 
+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
| 54          | 2              |
| 30          | 1              |
| 96          | 1              |
+-------------+----------------+

"""

import pandas as pd

from configuration import config

def find_customers(df_visits: pd.DataFrame, df_transactions: pd.DataFrame) -> pd.DataFrame:
    """ Find Customers

    Parameters:
        - df_visits *(dataframe)* - Data con las visitas de los clientes
        - df_transactions *(dataframe)* - Data con las transacciones de los clientes
    Returns:
        - df *(dataframe)* - Data resultado
    """

    df=df_visits[~df_visits['visit_id'].isin(df_transactions['visit_id'])]
    print(~df_visits['visit_id'].isin(df_transactions['visit_id']))
    print(df.groupby(by='customer_id').size().reset_index(name='count_no_trans'))

    return df.groupby(by='customer_id').size().reset_index(name='count_no_trans')

df_data_1 = pd.read_csv(config.di_routes["1581_1"],sep = "\t")
df_data_2 = pd.read_csv(config.di_routes["1581_2"],sep = "\t")

print(find_customers(df_data_1,df_data_2))
