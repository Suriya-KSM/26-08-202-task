#3.Fibonacci series using lambda function

#creating a function
def fibonacci(number):
    #initializing a local variable which holds list
    list1=[1,2]
    
    any(map(lambda _:list1.append(sum(list1[-2:])), range(2,number)))
    return list1[:number]


print(fibonacci(50))