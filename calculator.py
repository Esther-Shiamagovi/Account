def add(a,b):
    answer=a+b
    return answer

def subtract(c,d):
    result=c-d
    return result
def multiply(x,y):
    output= x*y
    return output

def divide(num1,num2):
    value=num1/num2
    return value

def remainder(o,p):
    remaining=o%p
    return remaining

def power_of(b,z):
    sum=b**z
    return sum
    
def sum(*numbers) : 
    total=0
    for number in numbers:
        total+=number 
        
    return total

def multiplication(*numbers):
    result=1
    for number in numbers:
        result*=number 
        
    return result

def creat_sentence(**words):
    print(words)
    sentence=""
    for word in words.values():
        sentence+=word
        sentence+=" "
        
    return sentence
  
   
def sum_and_greet(*args,**kwargs):
    total=0
    for number in args:
        total+=number
    first_name=kwargs['first_name']  
    last_name=kwargs['last_name']  
    greeting=f"Hello {first_name}{last_name},the sum is {total}"  
    
    return greeting

