with open("cars.txt", "r") as file:
    data = []
    for line in file:
        data.append(line)
print(data)
