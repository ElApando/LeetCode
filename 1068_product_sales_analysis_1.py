""" Product Sales Analysis I

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
 
Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.
 

Write a solution to report the product_name, year, and price for each sale_id in the Sales 
table.

Return the resulting table in any order.

The result format is in the following example.
 
Example 1:

Input: 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+

Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+

Output: 
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+

Explanation: 
From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.
"""

import pandas as pd

from configuration import config

def sales_analysis(df_sales: pd.DataFrame, df_product: pd.DataFrame) -> pd.DataFrame:
    """ Análisis de ventas

    Parameters:
        - df_sales *(dataframe)* - Dataframe con los datos de ventas
        - df_product *(dataframe)* - Dataframe con los datos de los productos
    Returns:
        - df_new *(dataframe)* - Dataframe con la unión de ambas tablas
    """

    df_new = pd.DataFrame()
    df_new = df_sales.merge(df_product, on='product_id', how='left')
    return df_new[["product_name","year","price"]]

df_data_1 = pd.read_csv(config.di_routes["1068_1"],sep = ",")
df_data_2 = pd.read_csv(config.di_routes["1068_2"],sep = ",")

print(sales_analysis(df_data_1,df_data_2))

# Finite Incantatem
 