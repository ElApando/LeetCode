""" Replace Employee ID Whit The Unique

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.

Table: EmployeeUNI

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+

(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the 
company.
Write a solution to show the unique ID of each user, If a user does not have a unique ID replace 
just show null.
Return the result table in any order.

The result format is in the following example.

Example 1:
Input: 
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+

EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+

Output: 
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+

Explanation: 
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.
"""

import pandas as pd

def replace_employee_id(df_employees: pd.DataFrame, df_employee_uni: pd.DataFrame) -> pd.DataFrame:
    """ Cambio de número de empleado

    Parameter:
        - df_employees *(DataFrame)* - DataFrame con el nombre de los empleados
        - df_employee_uni *(DataFrame)* -Dataframe con el ID de interés
    Return:
        - df_data *(DataFrame)* - Unión de ambas tablas
    """
    df_data = df_employees.merge(df_employee_uni, on='id', how='left')
    return df_data[["unique_id","name"]]

di_data_1 = {"id":[1,7,11,90,3],
             "name":["Alice","Bob","Meir","Winston","Jonathan"]}
df_data_1 = pd.DataFrame(di_data_1)

di_data_2 = {"id":[3,11,90],
             "unique_id":[1,2,3]}
df_data_2 = pd.DataFrame(di_data_2)

print(replace_employee_id(df_data_1, df_data_2))

# Finite Incantatem
 