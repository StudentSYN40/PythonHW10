def add_pet():
    # Ввод информации о питомце
    name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    # Заполнение словаря pets информацией о питомце
    pets[name] = {
        "Вид питомца": pet_type,
        "Возраст питомца": age,
        "Имя владельца": owner_name
    }


# Определение слова "год", "года" или "лет" в зависимости от возраста
def age_word(age):
    age_word = "лет"
    if age % 10 == 1 and age != 11:
        age_word = "год"
    elif 2 <= age % 10 <= 4 and (age < 10 or age > 20):
        age_word = "года"
    return age_word

# Создание пустого словаря pets
pets = {}

add_pet()

# Вывод информации о питомце в нужном формате
for pet in pets.keys():
    info_pet = pets[pet]
    pet_type = info_pet["Вид питомца"]
    age = info_pet["Возраст питомца"]
    owner_name = info_pet["Имя владельца"]
    print(f'Это {pet_type} по кличке "{pet}". Возраст питомца: {age} {age_word(age)}. Имя владельца: {owner_name}')
