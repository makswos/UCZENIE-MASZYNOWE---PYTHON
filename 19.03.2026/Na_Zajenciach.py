import kagglehub
import pandas as pd

path = kagglehub.dataset_download("spscientist/students-performance-in-exams")

file_path = path + "/StudentsPerformance.csv"
df = pd.read_csv(file_path)
# print(df.head())
# print(df.describe())
# print(df.shape)
# print(df.columns)

# Print the column names to check for typos
print(df.columns)

# Policz liczbe osob z każdej grupy rasowej:
# print(df['gender'].value_counts())

# print(df['test preparation course'].value_counts())
# print(df[df['test preparation course'] == "completed"].shape[0])

# Wyświetl tylko tych którzy mają zaliczony test z matematyki na powyżej 70 punktów:
# print(df[df['math score'] > 70])    

# Zadanie 2
# print(df[df['gender'] == "female"])
# print(df[df['writing score'] > 80])
# print(df[(df['gender'] == "female") & (df['writing score'] > 80)])


# print(df['parental level of education'].value_counts())

# print(df['parental level of education'].isin(["master's degree", "bachelor's degree"]))

# print(df[df['parental level of education'].isin(["master's degree", "bachelor's degree"])])

# df.groupby('gender')['reading score'].mean()

# zadanie 1: policz średnią w podziele na 'gender', ale ze wszystkich trzech testów
# w jednej tabeli

# df.groupby('gender')[['reading score', 'math score', 'writing score']].mean()
# df['total score'] = df['reading score'] + df['math score'] + df['writing score']
# print(df['total score'])

# print(df[['math score','reading score','writing score']].corr())

df_female = df[df['gender'] == "female"]
print(df_female)
