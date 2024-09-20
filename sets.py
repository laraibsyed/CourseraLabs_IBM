list = ["rap", "house", "electronic music", "rap"]
genres = set(list)
print(genres)

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print("The sum of A is: ", sum(A))
print("The sum of B is: ", sum(B))

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

album_set3 = album_set1.union(album_set2)
print(album_set3)

print(album_set1.issubset(album_set3))