# Kieran Seven
from dog import Dog

dog_list = []
with open("dogs.txt", "r") as file:
    for line in file:
        lst = line.split()
        tmp_dog = Dog(lst[0], lst[1], lst[2], lst[3])
        dog_list.append(tmp_dog)

print("--Original Dog Characteristics--")
print(dog_list[0].get_name())
print(dog_list[0].get_breed())
print(dog_list[0].get_trick())
print(dog_list[0].isHungry())

dog_list[0].speak()
dog_list[0].feed()
dog_list[0].change_trick("fetch")

print("--Modified Dog Characteristics--")
print(dog_list[0].get_name())
print(dog_list[0].get_breed())
print(dog_list[0].get_trick())
print(dog_list[0].isHungry())
