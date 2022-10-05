# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "filter_all_or_nothing_people" - kaip argumentą priims "users"
# sąrašą ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie arba neturi
# naminių gyvūnų visiškai, arba turi ir šunį, ir katę.

# 2. funkcija "filter_underaged_owners" - kaip argumentą priims "users" sąrašą
# ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie dar nėra pilnamečiai,
# bet turi bent vieną naminį gyvūną.

users = [
    { 'id': '1', 'name': 'John Smith', 'age': 17, 'hasDog': True, 'hasCat': True},
    { 'id': '2', 'name': 'Ann Smith', 'age': 24, 'hasDog': True, 'hasCat': False},
    { 'id': '3', 'name': 'Tom Jones', 'age': 63, 'hasDog': True, 'hasCat': True},
    { 'id': '4', 'name': 'Rose Peterson', 'age': 20, 'hasDog': True, 'hasCat': False},
    { 'id': '5', 'name': 'Alex John', 'age': 25, 'hasDog': False, 'hasCat': False},
    { 'id': '6', 'name': 'Ronald Jones', 'age': 31, 'hasDog': False, 'hasCat': True},
    { 'id': '7', 'name': 'Elton Smith', 'age': 16, 'hasDog': True, 'hasCat': False},
    { 'id': '8', 'name': 'Simon Peterson', 'age': 32, 'hasDog': False, 'hasCat': True},
    { 'id': '9', 'name': 'Daniel Cane', 'age': 15, 'hasDog': False, 'hasCat': False},
]

# 1
def filter_all_or_nothing_people(users):
    users_filtered = []
    for user in users:
        if user['hasDog'] == True and user['hasCat'] == True or user['hasDog'] == False and user['hasCat'] == False:
            users_filtered.append(user)
    print(users_filtered)
filter_all_or_nothing_people(users)

# 2
def filter_underaged_owners(users):
    kid_owners = []
    for kid in users:
        if kid['hasDog'] == True or kid['hasCat'] == True:
            if kid['age'] < 18:
                kid_owners.append(kid)
    print(kid_owners)
filter_underaged_owners(users)







# def filter_all_or_nothing_people(user):
#     if user["hasDog"] == True and user["hasCat"] == True:
#         return user
#     else:
#         pass
# filtered_user = filter(filter_all_or_nothing_people, users)
# for u in filtered_user:
#     print(dict(u)["name"])
#
#
# def filter_all_or_nothing_people():
#     filtered = list(filter(lambda user: user['hasDog'] == True and user["hasCat"] == True, users))
#     print(filtered)
# filter_all_or_nothing_people()






