import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:

    Lista = []
    for i in range(1,len(weather),1):

        if weather[" temperature "][i] > weather[" temperature "][i-1]:
            Lista.append(weather[" id "][i])

        elif weather[" temperature "][i-1] > weather[" temperature "][i]:
            Lista.append(weather[" id "][i-1])

        else:
            pass 

    weather_max = weather[weather[" id "].isin(Lista)]

    return weather_max[[" id "]].reset_index(drop = True)

BD1 = pd.read_excel("Prueba.xlsx")

Activo = rising_temperature(BD1)
print(Activo)
