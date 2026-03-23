import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=sns.load_dataset("titanic")
# print(df := sns.load_dataset("titanic"))

# Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
    #    'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
    #    'alive', 'alone'],
    #   dtype='str')


#Wyświetl liczbe pasażerów którzy przeżyli
# print(df[df.survived == 1].shape[0])


# #Wyświetl średnią cenę biletu dla każdej klasy
# print(df.groupby("pclass")["fare"].mean())


# #sprawdz w której kolumnie brakuje najwięcej danych
# print(df.isna().sum())


# #Wypełnij brakujące dane w kolumnie "age" średnią wartością wieku
# round(df["age"].mean(), 2)
# df["age"] = df["age"].fillna(round(df["age"].mean(), 2))


# print(df.isna().sum())


# #Stwórz nową kolumnę isAlone która przyjmie wartość 1 jeśli pasażer podróżował sam, a 0 w przeciwnym przypadku
# df["isAlone"] = ((df["sibsp"] + df["parch"]) == 0).astype(int)
# print(df)


# #wyświetl rekordy gdzie survived == 1 i alive == "yes"
# # print(df[(df.survived == 1) & (df.alive == "no")]) 
# # print(df[(df.survived == 0) & (df.alive == "yes")])


# print(df.head())


#ile osób płyneło w każdej klasie przedstaw to w prostym wykresie 



# mapa_klas = {1: "Pierwsza", 2: "Druga", 3: "Trzecia"}
# df["pclass"] = df["pclass"].map(mapa_klas)
# sns.countplot(x="pclass", order=["Pierwsza", "Druga", "Trzecia"], data=df)
# plt.title("Liczba pasażerów w każdej klasie", loc="center")
# plt.xlabel("Klasa")
# plt.ylabel("Liczba pasażerów")
# plt.show()



#wykres rozkładu wieku pasażerów


# sns.histplot(df["age"], bins=30, kde=True)
# plt.title("Rozkład wieku pasażerów", loc="center")
# plt.xlim(0, 80)
# plt.xlabel("Wiek")
# plt.ylabel("Liczba pasażerów")
# plt.show()



# Ile osób płyneło w podziale na kategorie:
# kategoria to: dziecko (poniżej 16 lat), kobieta, mężczyzna (od 16 roku życia)
# przedstaw to na prostym wykresie słupkowym
# df["kategoria"] = df.apply(
    # lambda row: "dziecko" if row["age"] < 16 else ("kobieta" if row["sex"] == "female" else "mężczyzna"),
    # axis=1,
# )
# sns.countplot(x="kategoria", data=df, order=["dziecko", "kobieta", "mężczyzna"])
# plt.title("Liczba pasażerów w każdej kategorii", loc="center")
# plt.xlabel("Kategoria") 
# plt.ylabel("Liczba pasażerów")
# plt.show()



# Upewnij się, że kolumna "kategoria" istnieje
# if "kategoria" not in df.columns:
#     df["kategoria"] = df.apply(
#         lambda row: "dziecko" if row["age"] < 16 else ("kobieta" if row["sex"] == "female" else "mężczyzna"),
#         axis=1,
#     )
# g = sns.catplot(
#     x="kategoria",
#     hue="survived",
#     col="pclass",
#     data=df,
#     kind="count",
#     order=["dziecko", "kobieta", "mężczyzna"],
#     hue_order=[0, 1],
#     col_order=[1, 2, 3],
#     height=4,
#     aspect=0.9,
# )
# g.set_axis_labels("Kategoria", "Liczba pasażerów")
# g.set_titles("Klasa biletu: {col_name}")
# g.figure.suptitle("Liczba pasażerów w każdej kategorii w podziale na przeżycie i klasę biletu", y=1.05)
# if g._legend is not None:
#     g._legend.set_title("Przeżył")
#     for text, label in zip(g._legend.texts, ["Nie", "Tak"]):
#         text.set_text(label)



# plt.tight_layout()
# plt.show()



#zrob wykres zależności przeżywalności zależną od klasy biletu w procentach
# g = sns.catplot(
#     data=df,
#     x="pclass",
#     y="survived",
#     hue="sex",
#     kind="bar",
#     estimator=lambda x: x.mean() * 100,
#     errorbar=None,
#     order=[1, 2, 3],
#     hue_order=["female", "male"],
#     height=4,
#     aspect=1.1,
# )

# g.set_axis_labels("Klasa biletu", "Procent przeżywalności")
# g.set(ylim=(0, 100))
# g.figure.suptitle("Przeżywalność (%) wg klasy biletu i płci", y=1.03)

# if g._legend is not None:
#     g._legend.set_title("Płeć")
#     for text, label in zip(g._legend.texts, ["Kobieta", "Mężczyzna"]):
#         text.set_text(label)

# plt.tight_layout()
# plt.show()


#wyświetl wykres pokazujący rozkład cen biletu w zależności od klasy
# sns.boxplot(x="pclass", y="fare",whis=0, data=df, order=[1, 2, 3])
# plt.title("Rozkład cen biletu w zależności od klasy", loc="center")
# plt.xlabel("Klasa biletu")
# plt.ylabel("Cena biletu")
# plt.ylim(0, 300)
# plt.show()


#zrob wykres przezywalności w zależności od ilości rodziny na pokładnie (rodzina to suma kolumn "sibsp" i "parch")
# df["family_size"] = df["sibsp"] + df["parch"]
# g = sns.catplot(
#     data=df,  
#     x="family_size",  
#     y="survived",
#     kind="bar",
#     estimator=lambda x: x.mean() * 100,
#     errorbar=None,
#     order=sorted(df["family_size"].unique()),
#     height=4,
#     aspect=1.2,
# )
# g.set_axis_labels("Rozmiar rodziny", "Procent przeżywalności")
# g.set(ylim=(0, 100))
# g.figure.suptitle("Przeżywalność (%) wg rozmiaru rodziny")
# plt.tight_layout()
# plt.show()
df['kategoria'] = df['sex']

df[df['age'] < 16]
df.loc[df['age'] < 16, 'kategoria'] = 'dziecko'
df['kategoria'].value_counts()
df['kategoria_int'] = df['kategoria'].map({'female': 0, 'male':  1, 'dziecko': 2})

correlation = df[['fare', 'age', 'pclass', 'kategoria_int']].corr()

sns.heatmap(correlation, annot=True, cmap='Blues')
plt.title('Mapa ciepła korelacji')
plt.show()




# ZADANIE DOMOWE:
# 1. flights lub diamonds i po 3 wykresy 