#positional arguments
def sum_multiplication(sum,multiplication):
    return(f"the sum of 6 and 2 is {sum} and their prodduct is {multiplication}")
print(sum_multiplication(6+4+2*4,6*5*8))

#keyword arguments
def names(firstname="a",secondname="b"):
    return (f"my name is {firstname} {secondname}")
print(names())
print(names("Winnie"))
print(names(firstname="Winnie", secondname="Sikinyi"))

# args-positional arguments
def firstname(*names):
    for name in names:
      print(f" hello {name}") 
firstname("rollsroyce","bmw","audi")
#final= [name for name in names]
# print(f" hello {final}")
        
def firstname(**names):
    for name in names.values():
     print(name)
firstname(a="Toyota",b="Auris",c="Landcruiser",d="v8") 

#Palindrone
name = "Winue"
print(name[::-1])
print(name[::-2])

