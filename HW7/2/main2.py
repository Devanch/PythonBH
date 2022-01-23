import pickle


class Person:
    name = "Tom"
 
    def display_info(self):
        print("Привет, меня зовут", self.name)
 
person1 = Person()


with open('simple2.txt', 'wb') as f:
    pickle.dump(person1, f)

with open('simple2.txt', 'rb') as f:
    person_new = pickle.load(f)

person_new.display_info()  
