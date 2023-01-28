#1 if
cars = ["audi","bmw","subaru","toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

#2 == != > < >= <=
car = "Audi"
if car.lower() == "audi":
    print("True")
else:
    print("False")

requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

age = 18

if age > 18:
    print("True")
else:
    print("False")
if age >= 18:
    print("True")
else:
    print("False")

#3 and or
age_0 = 18
age_1 = 30

if age_0 > 18 and age_1 == 30:
    print("True")
else:
    print("False")
if age_0 >= 18 and age_1 == 30:
    print("True")
else:
    print("False")
if age_0 > 18 or age_1 == 30:
    print("True")
else:
    print("False")
if age_0 > 18 and age_1 != 30:
    print("True")
else:
    print("False")

#4 in not
users = ["andrew","caroline","david"]
user = "zhangEnpei"
if user in users:
    print(f"Welcome here ,{user}.")
if user not in users:
    print(f"Sign up please.")

#5 bx
game_active = True
can_edit = False
print(game_active)

#6 if-elif-else
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

age = -32671902498

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

age = -32671902498

if 0 < age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")

#7 if--if
requested_toppings = ["mushrooms","extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni")

print("\nFinished making your pizza!")

#8 lx--if
available_toppings = ["mushrooms","olives","green peppers","pepperoni","pineapple","extra cheese"]
requested_toppings = ["mushrooms","french fries","extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry,we don't have {requested_topping}.")

print("\nFinished making your pizza!")