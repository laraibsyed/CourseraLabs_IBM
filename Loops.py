for count in range(-5,6):
    print(count)

Genres = ["rock", "R&B", "Soundtrack", "R&B", "Soul", "Pop"]
for genre in Genres:
    print(genre)

squares = ["Red", "Yellow", "Green", "Purple", "Blue"]
for square in squares:
    print(square)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
rating = PlayListRatings[0]
i = 0
while(i < len(PlayListRatings) and rating >= 6):
    print(rating)
    i = i + 1 
    rating = PlayListRatings[i]   

colours = ["orange", "orange", "purple", "blue", "orange"]
new_colours = []
current = 0
while(current < len(colours) and colours[current] == "orange"):
    new_colours.append(colours[current])
    current = current + 1
print(new_colours)

print("Six Multiplication")
count = 1
for num in range(10):
    print("6 x", count, " = ", 6 * count)
    count = count + 1

print("Seven Multiplication")
i = 1
for num in range(10):
    print("7 x", i, " = ", 7 * i)
    i = i + 1

animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
New = []
i=0
while i<len(animals):
    j=animals[i]
    if(len(j)==7):
        New.append(j)
    i=i+1
print(New)