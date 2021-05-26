import pandas as pd
file = "data.csv"
pd.read_csv(file)

df = pd.read_excel(file) # dataframe
df.head()
 # fiest 5 rows of file

songs = {"hipho":22,"classical":22}
df =pd.DataFrame(songs)
coloum = df['coloum1']
booleanoncaloum = df['coloum1'] > 10 # fives result as true or false for caloum
coloum.unique() # gives dist values of coloumn

df.to_csv("modified.csv")


# loc gets rows (and/or columns) with particular labels.
#
# iloc gets rows (and/or columns) at integer locations.
