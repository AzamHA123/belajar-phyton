print("to do list")

active = 'y'

while active=='y':
  list = input("list? = ")
  file = open('todolist.txt', 'a')
  file.write(list+"\n")
  file.close()
  file = open('todolist.txt', 'r')
  print(file.read())
active = input('done (y/n)')
