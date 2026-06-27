""" Article Views I

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+

There is no primary key (column with unique values) for this table, the table may have duplicate
 rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on
 some date. 
Note that equal author_id and viewer_id indicate the same person.
 
Write a solution to find all the authors that viewed at least one of their own articles.
Return the result table sorted by id in ascending order.
The result format is in the following example.

Example 1:
Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+

Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
"""

import pandas as pd

from configuration import config

def article_views(df_views: pd.DataFrame) -> pd.DataFrame:
    """ Da las vistas de los artículos

    Parameters:
        - 
    Returns:
        - 
    """
    df_response = pd.DataFrame()
    df_order = df_views.loc[df_views["author_id"] == df_views["viewer_id"]]
    df_response["id"] = df_order["author_id"].unique()

    return df_response.sort_values(by="id", ascending=True)

DataFrame = pd.read_csv(config.di_routes["1148"], sep=",")
print(article_views(DataFrame))

# Finite Incantatem
