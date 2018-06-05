import random

def generate_random_number():
    return str(random.randint(0,5))

print(generate_random_number())
print(generate_random_number()+"-"+generate_random_number())
