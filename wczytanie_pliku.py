import pandas as pd

tab = pd.read_excel(r"C:\Users\monia\PycharmProjects\Arkusz kalkulacyjny bez tytułu.xlsx")

print("Tabela zaimportowana z pliku: ")
print(tab)

print(tab[['wiek', 'wartosc']].describe())


tab['ostatnia_litera'] = tab['imie'].str[-1]



i=0
while i < tab.shape[0]:
    if tab.at[i,'ostatnia_litera'] =='a':
        tab.at[i,'plec']='Kobieta'
    else:
        tab.at[i,'plec']='Mężczyzna'
    i=i+1

del tab['ostatnia_litera']
print (tab)



tab_k = tab[tab['plec'] == 'Kobieta']
tab_m = tab[tab['plec'] == 'Mężczyzna']

print("Statystyki dla kobiet: ")
print(tab_k[['wiek', 'wartosc']].describe())
print("Statystyki dla mężczyzn: ")
print(tab_m[['wiek', 'wartosc']].describe())

print('Za 12 lat osoby z rejestru będą w wieku: ')
tab['wiek za 12 lat'] = tab['wiek'] + 12
print(tab)


tab.to_excel('Nowy rejestr.xlsx', index=False)