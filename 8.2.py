import pandas as pd

data = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/', header=0)

data[0] = data[0].rename(columns={'TITLE':'TYTUŁ', 'ARTIST':'ARTYSTA', 'YEAR':'ROK', 'HIGH POSN':'MAX POZ'})

liczba_artystow = data[0]['ARTYSTA'].nunique()

najczestsze_zespoly = data[0]['ARTYSTA'].value_counts()

data[0] = data[0].rename(columns=lambda x: x.title())

data[0] = data[0].drop(columns='Max Poz')

liczba_albumow_na_rok = data[0]['Rok'].value_counts()
najczestszy_rok = liczba_albumow_na_rok.idxmax()

albumy_1960_1990 = data[0][(data[0]['Rok'] >= 1960) & (data[0]['Rok'] <= 1990)]
liczba_albumow_1960_1990 = len(albumy_1960_1990)

najmlodszy_album_rok = data[0]['Rok'].max()

najwczeniej_wydane_albumy = data[0].groupby('Artysta').agg(Rok=('Rok', 'min')).reset_index()





print(data[0])
print("\nLiczba pojedynczych artystów na liście:", liczba_artystow)
print("\nNajczęściej występujące zespoły na liście:", najczestsze_zespoly.head(10))
print("\nRok z największą liczbą albumów na liście:", najczestszy_rok)
print("\nLiczba albumów wydanych między 1960 a 1990 rokiem włącznie:", liczba_albumow_1960_1990)
print("\nNajmłodszy album na liście został wydany w roku:", najmlodszy_album_rok)
print("\nLista najwcześniej wydanych albumów dla każdego artysty:")
print(najwczeniej_wydane_albumy)