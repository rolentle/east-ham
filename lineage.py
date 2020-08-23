import simpy
env = simpy.Environment()

class Person:
    def __init__(self,name, age, gender):
        self.name = name
        self._age = age
        self.gender = gender

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


def greet(env, person):
    while True:
        name = person.name
        age = person.age
        msg = f"My name is {name}, I am {age} years old"
        print(msg)
        person.age += 1
        if  person.age % 2 == 0:
            yield env.timeout(1)

if __name__ == "__main__":
    person = Person("Rolen", 33, "male")
    env.process(greet(env, person))
    env.run(until=5)
