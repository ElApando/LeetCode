import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:

    Nueva_DB = pd.DataFrame()
    Nueva_DB = employees.merge(employee_uni, on='id', how='left')
    return Nueva_DB[["unique_id","name"]]

Employees = {"id":[1,7,11,90,3],
             "name":["Alice","Bob","Meir","Winston","Jonathan"]}
Employees = pd.DataFrame(Employees)

EmployeeUNI = {"id":[3,11,90],
               "unique_id":[1,2,3]}
EmployeeUNI = pd.DataFrame(EmployeeUNI)

Activo = replace_employee_id(Employees,EmployeeUNI)
print(Activo)


 