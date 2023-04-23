
# Write a function that uses while, if and continue statements to 
# print all the even numbers between 0 and 50
def even_number():
    x=0
    while x <=50:
       x+=1
       if x %2!=0:
            continue
       print(x)


#qn2Write a function that takes an integer argument and prints "Prime" if 
# the number is prime, and "Not prime" if the number is not prime.
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


#qn3Write a function that takes a list of integers as input and prints the 
# sum of all the even numbers in the list.
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

#qn 4Write a function that takes any two integers as input, and prints the sum of all
#  the numbers between the two integers (inclusive) that are divisible by 3    
def integer(y,z):
   sum = 0
   x = range(y,z+1)
   for i in x:
      if i%3==0:
         sum+=1
         print( sum)

       
    

    
    
 