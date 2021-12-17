from collections import Counter

g = persons = [
    {
        "name": "Anna",
        "age": 25,
        "gender": "female"
    }, {
        "name": "Feris",
        "age": 31,
        "gender": "male"
    }, {
        "name": "Keanu",
        "age": 57,
        "gender": "male"
    }, {
        "name": "Angelina",
        "age": 46,
        "gender": "female"
    }, {
        "name": "Flex",
        "age": 42,
        "gender": "male"
    }, {
        "name": "Cortana",
        "age": 25,
        "gender": "female"
    },  {
        "name": "Keanu",
        "age": 57,
        "gender": "male"
    }, {
        "name": "Angelina",
        "age": 46,
        "gender": "female"
    }, {
        "name": "Keanu",
        "age": 42,
        "gender": "male"
    }, {
        "name": "Cortana",
        "age": 25,
        "gender": "female"
    }
]

list_names = list()
list_age = list()
list_male35 = list()
cnt_male = 0;
cnt_female = 0;
cnt_adult = 0;

how_many_people = len(persons);
   
for pers in persons:
    name = pers.get("name")
    gender = pers.get("gender")
    age = pers.get("age")
    list_names.append(name)
    list_age.append(age)
    if gender == "male":  cnt_male  += 1 
    if gender == "female":  cnt_female  += 1
    if age > 17: cnt_adult += 1 
    if (gender == "male") and (age > 35) and (name[0] == 'F'): list_male35.append(name)
    
my_dict = {name:list_names.count(name) for name in list_names}
sorted_x = sorted(my_dict.items(), key=lambda val: val[1], reverse=True)

list_age.sort()
print(f"1.Количество всех людей: {how_many_people}")
print(f"2.Кол-во мужчин: {cnt_male}, Кол-во женщин {cnt_female}");
print(f"3.Совершеннолетние: {cnt_adult}");
print(f"4.Список людей: {list_names}");
print(f"5.Список возрастов людей: {list_age}");
print(f"6a.Наиболее популярные имена: {sorted_x[:3]} ")
print(f"6b.Наиболее популярные имена: {Counter([pers.get('name') for pers in persons]).most_common(3)} ")
print(f"7.Список мужчин старше 35 имена которых начинаются с F: {list_male35}");