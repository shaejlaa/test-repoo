name = input("Whom should I assign this to?")
filename =input("Where shall I save it?")

with open(filename, "w") as f:
    f.write("Hi" + name + "\nWe hope you enjoy learning Python with us!\n\nBest,\nTh3 3l337 AP Computer Science Team")

with open(filename, "r") as f:
    print(f.read())
