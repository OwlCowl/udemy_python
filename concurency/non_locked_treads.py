counter = 0

def increment_counter():
    global counter
    counter +=1
    print(counter)
    print("--------")

for x in range(10):
    increment_counter()

increment_counter()

