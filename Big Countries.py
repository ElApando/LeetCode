import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    Mundo = pd.DataFrame()
    world = world[["name","area","population"]]
    Mundo = world.loc[(world["area"] >= 3000000) | (world["population"] >= 25000000)]

    return Mundo

DataFrame = pd.read_excel("Prueba.xlsx")

Activo = big_countries(DataFrame)
print(Activo)