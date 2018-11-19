def score(w):
    w = w.lower()
    d = {"aeioulnrst": 1, "dg": 2, "bcmp": 3, "fhvwy": 4, "k": 5, "jx": 8, "qz":10}
    points = 0
    for key in d.keys():
        for char in w:
            if char in key:
                points = points + d[key]
    return points

print(score("hello"))
print(score("Nursima"))
            
        