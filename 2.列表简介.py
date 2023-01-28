#1 lx
bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles)

print(bicycles[0])
print(bicycles[-1])

print(bicycles[0].title())

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#2 lx[nx] = txt
motorcycles = ["honda","yamaha","suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

#3 .append(txt)
motorcycles = ["honda","yamaha","suzuki"]
motorcycles.append("ducati")
print(motorcycles)

#4 .insert(nx,txt)
motorcycles = ["honda","yamaha","suzuki"]
motorcycles.insert(0,"ducati")
print(motorcycles)

#5 del lx[nx]
motorcycles = ["honda","yamaha","suzuki"]
del motorcycles[1]
print(motorcycles)

#6 .pop(nx)
motorcycles = ["honda","yamaha","suzuki"]
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ["honda","yamaha","suzuki"]
popped_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycles)

#7 .remove(txt)
motorcycles = ["honda","yamaha","suzuki","ducati"]
motorcycles.remove("ducati")
print(motorcycles)

motorcycles = ["honda","yamaha","suzuki","ducati"]
example = "ducati"
motorcycles.remove(example)
print(motorcycles)
print(example)

#8 .sort(reverse=bx)
cars = ["bmw","audi","toyota","subaru"]
cars.sort()
print(cars)

cars = ["bmw","audi","toyota","subaru"]
cars.sort(reverse=True)
print(cars)

#9 .sorted(lx)/sorted(lx,reverse=bx)
cars = ["bmw","audi","toyota","subaru"]
print(sorted(cars))
print(cars)

print(sorted(cars,reverse=True))
print(cars)

#10 .reverse()
cars = ["bmw","audi","toyota","subaru"]
cars.reverse()
print(cars)

#11 len(lx)
cars = ["bmw","audi","toyota","subaru"]
print(len(cars))