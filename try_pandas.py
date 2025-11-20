import pandas as pd

contacts = pd.DataFrame(
    {
        "name": [
            "Allen Raymond",
            "Chaim Lewis",
            "Kennedy Lane",
            "Wylie Pope",
            "Cyrus Jackson",
        ],
        "email": [
            "nulla.ante@vestibul.co.uk",
            "dui.in@egetlacus.ca",
            "mattis.Cras@nonenimMauris.net",
            "est@utquamvel.net",
            "nibh@semsempererat.com",
        ],
        "phone": [
            "(992) 914-3792",
            "(294) 840-6685",
            "(542) 451-7038",
            "(692) 802-2949",
            "(501) 472-5218",
        ],
        "favorite": [False, False, True, False, True],
    },
    index=[1, 2, 3, 4, 5],
)


contacts.to_excel("./excel/contacts.xlsx", sheet_name="Contacts")
# Примітка: для запису даних на кілька листів, необхідно створити об'єкт pd.ExcelWriter та викликати метод to_excel для кожного об'єкта.

# contacts.to_csv("./excel/users.csv", index=False)

# print(contacts)
# print(contacts["name"])
# print(contacts.loc[3])
# print(contacts[contacts["favorite"]])
# print(contacts.iloc[0:3])
