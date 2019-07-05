# coding=utf-8
print('come in test1')

def calculater():
    a = 1
    b = 2
    print(a + b)

class StudentGroup(object):
    level = 'collage'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get(self):
        return 'this is ' + self.name + ' and I am ' + str(self.age) + ' years old'

class Cat(object):
    species = '猫科动物'
    leg_amount = 4
    
    def __init__(self, name, color, num):
        self.name = name
        self.color = color
        self.age = num

    def eat_rat(self, amount):
        if (amount > 4):
            return 'no, too many rats!!!!!'
        else:
            print('Cat can eat ' + str(amount) + ' rats')


if __name__ == "__main__":
    # calculater()
    martin = StudentGroup('matrin', 26)
    my_cat = Cat('coffee', 'blue', 1)
    print(martin.level)
    print(martin.get())
    print(my_cat.eat_rat(2))
    # %s: str; %d: int; %f: float
    print("my cat's name is %s, and it is %d years old" % (my_cat.name, my_cat.age))
    print(my_cat.species)

