#1 for:
magicians = ["alice","david","carolina"]
for magician in magicians:
    print(magician)
print(magicians)

#2 range(nx,nx,nx)
example = range(1,5)
for value in range(1,5):
    print(value)
for value in range(5):
    print(value)
for value in range(1,5,2):
    print(value)

example = list(range(1,10,2))
print(example)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

#3 min(lx) max(lx) sum(lx)
digits = list(range(1,10))
print(digits)
smallest = min(digits)
biggest = max(digits)
summation = sum(digits)
print(smallest,biggest,summation)

#4 lx[nx:nx]
players = ["charles","martina","michael","florence","eli"]
print(players[0:3])
print(players[:3])
print(players[0:])
print(players[-1:])
print(players[0:4:2])

for player in players[0:3]:
    print(player.title())

#5 lx = lx[nx:nx]
my_foods = ["pizza","falafel","carrot cake"]
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice cream")
print(my_foods)
print(friend_foods)

#6 tx
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200,)
print(dimensions[0])

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

dimensions = (100,40)
print(dimensions)