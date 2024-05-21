import pandas as pd
import numpy as np

def find_products(customer: pd.DataFrame) -> pd.DataFrame:
	
	customer = customer.loc[customer["referee_id"] != 2]
	print(customer.loc[~customer["referee_id"].isin([np.nan])])
	print(customer.loc[~customer["referee_id"].isin([2])][["name"]])

	return customer[["name"]]

Diccionario = {"id ":[1,2,3,4,5,6],"name":["Will","Jane","Alex","Bill","Zack","Mark"],"referee_id":[np.nan,np.nan,2,np.nan,1,2]}
# dataframe = pd.DataFrame(Diccionario)
dataframe = pd.read_excel("Prueba.xlsx")
Activo = find_products(dataframe)

# print(Activo)


    

