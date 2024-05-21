import pandas as pd 

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    
    Busca = products.loc[products["low_fats"] == products["recyclable"]]
    Busca = Busca.loc[Busca["low_fats"] == "Y"]
    print(Busca.columns,type(Busca))

    return Busca[["product_id"]]

Diccionario = {"product_id":[0,1,2,3,4],"low_fats":["Y","Y","N","Y","N"],"recyclable":["N","Y","Y","Y","N"]}
dataframe = pd.DataFrame(Diccionario)
print(type(dataframe))
Activo = find_products(dataframe)

print(type(Activo))