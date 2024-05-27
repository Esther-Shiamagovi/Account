def print_numbers(n):
    numbers=range(n)
    for number in numbers:
        print(number)
        
def print_odd_numbers(n):
    numbers= range(n)
    for number in numbers:
        if number % 2!=0:
            print(number)
            
            
       
def print_even_numbers(n):
    numbers= range(n)
    for number in numbers:
        if number % 2==0:
            print(number)  
            

def odd_even(n):
    numbers= range(n)
    for number in numbers:
         if number % 2==0:
             print(f"{number} is even")
         else:
             print(f"{number} is not even") 
             



def check_divisibility(n):
    numbers= range(n)
    for number in numbers:
         if number % 2==0:
             print(f"{number} is divisible by 2")
         elif number%3 ==0:
             print(f"{number} is divisible by 3")
         elif number%5 ==0:
             print(f"{number} is divisible by 5")  
         else:
             print(f"{number} is not diviible by 2,3 or 5")  
    
    
             


def fizz_buzz(n):
    numbers= range(n)
    for number in numbers:
         if number % 3==0:
             print("fizz")
         elif number%5 ==0:
             print("buzz") 
         else:
             print("fizzbuzz")  

          
def countdown(n):
    while n>0:
         print(n)
    n-=1
    
def count_down_to_five(n):
    while n>0:
        print(n)
        if n==5:
            break
        n-=1
        
def divisible_by_seven(n):
    x=0
    while x<=n:
        x+=1
        if x%7 !=0:
            continue
        print(f"{x} is divisible by")

    
        
        
    
        
def get_oddnumbers():
    num = 0
    while num <= 100:
        if num % 2 != 0:
         print(num, end=",")
    num+=1
    
def odd_hundred():
    x=0
    while x<=100:
        x+=1
        if x%2 ==0:
            continue
    print(f"{x} is and odd number")
     
   
    
    
    
    
 