""" Recyclable and Low Fat Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' 
means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable 
and 'N' means it is not.
 
Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The result format is in the following example.

Example 1:
Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.

"""

import pandas as pd

def find_products(df_products: pd.DataFrame) -> pd.DataFrame:
    """ Coincidencia de productos 

    Parameters:
        - df_products *(dataframe)* - Dataframe con todos los productos
    Results:
        - df_data *(dataframe)* - Dataframe filtrado
    """

    df_data = df_products.loc[df_products["low_fats"] == df_products["recyclable"]]
    df_data = df_data.loc[df_data["low_fats"] == "Y"]

    return df_data[["product_id"]].reset_index(drop=True)

di_data = {"product_id":[0,1,2,3,4],
           "low_fats":["Y","Y","N","Y","N"],
           "recyclable":["N","Y","Y","Y","N"]}
dataframe = pd.DataFrame(di_data)

print(find_products(dataframe))

# Finite Incantatem
