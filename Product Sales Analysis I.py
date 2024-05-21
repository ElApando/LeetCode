import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    Nueva_DB = pd.DataFrame()
    Nueva_DB = sales.merge(product, on='product_id', how='left')
    return Nueva_DB[["product_name","year","price "]]

BD1 = pd.read_csv("BD1.txt",sep = "\t")
BD2 = pd.read_csv("BD2.txt",sep = "\t")

Activo = sales_analysis(BD1,BD2)
print(Activo)


 