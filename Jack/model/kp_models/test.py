dataset = []

with open("data.csv","r") as f:
    dataset = f.readlines()


print(len(dataset),len(dataset[4]))