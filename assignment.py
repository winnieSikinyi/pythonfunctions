def even_number():
    x=0
    while x < 50:
       x+=1
       if x %2!=0:
        continue
    print(x)
even_number()


#qn2
def prime_number():
   x = 12
   if x>1:
      for i in range(2,int(x/2)+1):
         if x%i ==0:
            print(x,"is not prime")
   else:
      print(x,"is prime")
prime_number()

#qn3
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

#qn 4
def add_two_integers():
   x = range (20,30)
   sum=0
   for i in x :
      if i %3==0:
         print(sum)
      else:
         print("num")
         sum = sum+1
add_two_integers()
       
        
       
    

    
    
 