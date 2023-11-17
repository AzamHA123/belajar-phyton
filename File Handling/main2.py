file= open('contoh.txt','r')
print(file.read())

# file= open('contoh.txt','w')
# file.write("a")
# file.close()

file= open('contoh.txt','a')
file.write("a")
file.close()