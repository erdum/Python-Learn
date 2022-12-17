a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

# When two strings are added they concatinate!
# A string and integer/float can't be added!
# we can do typecasting and can change the type of variables 


print(f"The sum is {a+b}")
print(f"The sub is {a-b}")
print(f"The product is {a*b}")
if b==0:
    print("Division is not possible")
else:
    print(f"The division is {a/b}")

print(type(a))
