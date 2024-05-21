import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    tweets["Tamaño"] = tweets["content"].apply(lambda X: len(X))
    tweets = tweets.loc[tweets["Tamaño"] > 15]

    return tweets[["tweet_id"]]

DataFrame = pd.read_excel("Prueba.xlsx")

Activo = invalid_tweets(DataFrame)
print(Activo)