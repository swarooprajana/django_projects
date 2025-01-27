j = open("file.txt", "a")
k = j.write(" don't open it")
print(k)
j.close()
g = open("file.txt", "r")
k = g.read()
print(k)
g.close()


