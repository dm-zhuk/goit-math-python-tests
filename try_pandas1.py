import pandas as pd

# users = pd.read_csv("./excel/users.csv")

# print(users)

# persons = pd.read_excel("./excel/persons.xlsx")

# print(persons)

employees = pd.read_json("./json/split.json", orient="split")

print(employees)
