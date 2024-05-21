import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df=visits[~visits['visit_id'].isin(transactions['visit_id'])]
    print(~visits['visit_id'].isin(transactions['visit_id']))
    print(df.groupby(by='customer_id').size().reset_index(name='count_no_trans'))

    return df.groupby(by='customer_id').size().reset_index(name='count_no_trans')

    # Diccionario = {"customer_id":[],"count_no_trans":[]}
    # Bandera = True

    # for i in range(0,len(visits),1):
    #     if visits["visit_id"][i] not in transactions['visit_id'].unique() and visits["customer_id"][i] not in Diccionario["customer_id"]:
    #         Diccionario["customer_id"].append(visits["customer_id"][i])
    #         Diccionario["count_no_trans"].append(1)

    #     elif visits["visit_id"][i] not in transactions['visit_id'].unique() and visits["customer_id"][i] in Diccionario["customer_id"]:
    #         Diccionario["count_no_trans"][Diccionario["customer_id"].index(visits["customer_id"][i])] = Diccionario["count_no_trans"][Diccionario["customer_id"].index(visits["customer_id"][i])]+1

    #     else:
    #         print(123)

    #     Nuevo = pd.DataFrame(Diccionario)
    #     Nuevo = Nuevo.sort_values(by='count_no_trans', ascending=False)
    #     Nuevo = Nuevo.reset_index(drop=True)

    # return Nuevo

BD1 = pd.read_csv("BD1.txt",sep = "\t")
BD2 = pd.read_csv("BD2.txt",sep = "\t")

Activo = find_customers(BD1,BD2)
print(Activo)
