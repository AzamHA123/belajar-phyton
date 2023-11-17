print("kalkulator sederhana")
print("====================")

# buat fungsi
  # tambah
def p(x,y):
  result = x + y
  return str(x) + "+" + str(y) + "=" +  str(result)
# kurang
def m(x,y):
  result = x - y
  return str(x) + "-" + str(y) + "=" +  str(result)
# bagi
def db(x,y):
  result = x / y
  return str(x) + "/" + str(y) + "=" +  str(result)
# kali
def t(x,y):
  result = x * y
  return str(x) + "*" + str(y) + "=" +  str(result)

# app
while True:
  print("pilih mode")
  print("1.  tambah")
  print("2.  kurang")
  print("3.  bagi")
  print("4.  kali")
  ans = int(input("1/2/3/4 "))
  if ans==1:
    n1= int(input("n1 "))
    n2= int(input("n2 "))
    print(p(n1,n2))
  elif ans==2:
    n1= int(input("n1 "))
    n2= int(input("n2 "))
    print(m(n1,n2))  
  elif ans==3:
    n1= int(input("n1 "))
    n2= int(input("n2 "))
    print(db(n1,n2))
  elif ans==4:
    n1= int(input("n1 "))
    n2= int(input("n2 "))
    print(t(n1,n2))