""" Big Countries
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it 
belongs, its area, the population, and its GDP value.

A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write a solution to find the name, population, and area of the big countries.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
Output: 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
"""

import pandas as pd
from configuration import config 

def big_countries(df_world: pd.DataFrame) -> pd.DataFrame:
    """Grandes Ciudades

    La función tiene como finalidad obtener las ciudades grandes que hay en los datos que se 
    ingresan

    Parameters:
        - df_world (dataframe) - Dataframe de datos crudos
    Returns:
        - df_save (dataframe) - Dataframe con los valores de interés
    """

    df_save = pd.DataFrame()
    df_world = df_world[["name","area","population"]]
    df_save = df_world.loc[(df_world["area"] >= 3000000) | (df_world["population"] >= 25000000)]

    return df_save

df_data = pd.read_csv(config.di_routes["595"])
print(big_countries(df_data))

# Finite Incantatem
