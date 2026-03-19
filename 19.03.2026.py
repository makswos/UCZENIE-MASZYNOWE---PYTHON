import kagglehub
import pandas as pd

path = kagglehub.dataset_download("spscientist/students-performance-in-exams")

file_path = path + "/StudentsPerformance.csv"
df = pd.read_csv(file_path)
# print(df.head())
# print(df.describe())
# print(df.shape)
# print(df.columns)

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


# Zadanie 3
# Znajdź wszystkich ktorzy napisali test z pisan ia na powyżej 90 lub test z czytania na powyżej 90:
print(df[(df['writing score'] > 90) | (df['reading score'] > 90)])
