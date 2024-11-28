import pandas as pd

tab = pd.read_excel(r"C:\Users\monia\PycharmProjects\Arkusz kalkulacyjny bez tytułu.xlsx")

print(tab)

print (tab.describe())


tab["ostatnia_litera"] = tab['imie'].str[-1]

i=0
while i < tab.shape[0]:
    if tab["ostatnia_litera"].str[-1] == "a":
        tab["płeć"]=["Kobieta"]
    else:
        tab["płeć"]=["Mężczyzna"]
    i=i+1