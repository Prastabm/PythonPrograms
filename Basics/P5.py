import random

# program to simulate

print("enter 1 to roll dice")
print("enter 0 to stop")
d1 = 0
d2 = 0
roll = int(input("enter choice: "))
while roll:
    if roll > 1:
        break
    print("d1: ", random.randint(1, 6), " d2: ", random.randint(1, 6))
    roll = int(input("enter choice: "))
