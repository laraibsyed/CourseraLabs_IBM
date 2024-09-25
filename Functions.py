def divide(a, b):
    return (a / b)

print(divide(20, 4))

def counting(str, keyword):
    words = []

    words = str.lower().split()

    dict = {}

    for key in words:
        if(key == keyword):
            dict[key] = words.count(key)
    
    print("Total Count", dict)

counting("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","little")
