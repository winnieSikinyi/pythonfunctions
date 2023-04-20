def year_of_birth (name,age):
    year = 2023-age
    print(f"Hello{name},you were born in {year}")

def mycountry(country ="Kenya"):
    print(f"Hello you are from {country}")
    
def hello(*names):
    for name in names:
     print(f"Hello {name}")

def sum(*nums):
   answer = 0
   for num in nums:
      answer+= num
      return answer
   
def multiplymany(**kwargs):
    answer = 1
    for num in kwargs.values():
       answer *=num
    return answer

def concatinate_args(*strs ):
    answer = ""
    for string in strs:
       answer+= string
    return answer
    

    
def concatinate_kwargs(**book): 
    answer = ""
    for length in book.values():
       answer +=length
    return answer


   

   