""" Rising Temperature

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+

id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.

Write a solution to find all dates' id with higher temperatures compared to its previous dates
 (yesterday).
Return the result table in any order.
The result format is in the following example.

Example 1:
Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+

Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+

Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
"""
import pandas as pd
from configuration import config

def rising_temperature(df_weather: pd.DataFrame) -> pd.DataFrame:
    """ Temperatura alta

    Parameters:
        - df_weather *(DataFrame)* - Data raw de temperatura
    Returns:
        - df_weather *(DataFrame)* - Data gold de temperatura
    """

    ls_save = []

    for i in range(1,len(df_weather),1):
        if df_weather["temperature"][i] > df_weather["temperature"][i-1]:
            ls_save.append(df_weather["id"][i])

        elif df_weather["temperature"][i-1] > df_weather["temperature"][i]:
            ls_save.append(df_weather["id"][i-1])

    df_weather_max = df_weather[df_weather["id"].isin(ls_save)]

    return df_weather_max[["id"]].reset_index(drop = True)

df_data = pd.read_csv(config.di_routes["197"])
print(rising_temperature(df_data))

# Finite Incantatem
