
# Write a function that uses while, if and continue statements to 
# print all the even numbers between 0 and 50
# def even_number():
#     x=0
#     while x <=50:
#        x+=1
#        if x %2!=0:
#             continue
#        print(x)
def even_number():
    x = 0
    while x <=50:
        x+=1
        if x %2!=0:
            continue
    print(x)   


# #qn2Write a function that takes an integer argument and prints "Prime" if 
# # the number is prime, and "Not prime" if the number is not prime.
num = 17
def checkPrime(num,iter=2):
  if num == iter:
    return True
  if num%iter==0:
    return False
  if num<2:
    return False
  return checkPrime(num,iter+1)
if checkPrime(num)==True:
  print("Prime")
else:
  print("Not Prime")

  def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
if is_prime(n):
    print("Prime")
else:
    print("Not prime")


# #qn3Write a function that takes a list of integers as input and prints the 
# # sum of all the even numbers in the list.
def list_integer():
   x=range(20,50)
   sum=0
   for i in x:
      if i%2==0:
         print(sum)
         sum=sum+1
      else:
         print("number")
   print(sum)  
list_integer()

# # #qn 4Write a function that takes any two integers as input, and prints the sum of all
# # #  the numbers between the two integers (inclusive) that are divisible by 3    
def integer(y,z):
   sum = 0
   x = range(y,z+1)
   for i in x:
      if i%3==0:
         sum+=1
         print( sum)
number = 6
if number>5:
   print(number*number)

# password = input("Enter password") 
# if password =="PYnative@#29":
#    print("Correct password") 
# else:
#    print("Incorrect Password")   

# # def user_check(choice):
# #    if choice == 1:
# #       print('Admin')
#     elif choice == 2:
#       print('Editor')
#     elif choice ==3:
#       print('Guest')
#     else:
#       print('Wrong entry') 

# num1 = 56
# num2 = 16
#  if num1>=num2:
#    print(num1,'and',num2,'are equal')
#    else:
#    print(num1,'is greater than',num2)
# else:
#    print(num1,'is smaller than',num2)
  # identation  
    
# x = 1
# while x <= 5: print(x,end=''): x = x+1
for i in range (1,11):
   print(i)
  #  patterns
rows = 6
for i in range(rows):
   for j in range(i):
      print(i,end='')
print('')

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def Order(self, items):
        total = 0
        for item in items:
            total += item['product'].price * item['quantity']
        print(f"Order Total: ${total}")

items = [{'product': Product('Product1', 10, 'Description1'), 'quantity': 2},
         {'product': Product('Product2', 20, 'Description2'), 'quantity': 3}]

product = Product('Product3', 30, 'Description3')
product.Order(items)

class Product:
    def __init__(self,name,price,description,category):
        self.name=name
        self.price=price
        self.description =description
        self.category = category

    def order(self,items):
        self.items = items
        self.total_price = sum([item['product'].price * item['quantity'] for item in items])
        print(f"Order")
        
    def set_category(self, category):
        self.category = category


items = [{'product': Product('Product1', 10, 'Description1'), 'quantity': 2},
         {'product': Product('Product2', 20, 'Description2'), 'quantity': 3}]

product = Product('Product3', 30, 'Description3')
product.set_category('Category3')
product.order(items)