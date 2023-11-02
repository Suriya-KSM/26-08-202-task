# To check whether the every elements in the given list is string or integer

#initializing the list
data = ['10', '501', '22', '37']

#checking the elements of the list is integer using lambda, isdigit function
result=list(filter(lambda x: x.isdigit(), data))

#printing the result
if result == data:
    print("Every element in the list is a Integer")
else:
    print("Elements in the list also has string")