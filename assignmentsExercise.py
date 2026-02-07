x,y,z = 2,5,10
numbers = 1,5,7,10,6

#Get 2 numbers from user and multiplicate them - (x+y+z)

first_number = int(input("First number: "))
second_number = int(input("Second number: "))
multiplication_numbers = first_number*second_number
result = multiplication_numbers - (x+y+z)
print(result)


# y / x
print(y//x)

# (x+y+z) % 3
sumOfNumbers = x+y+z
print(sumOfNumbers%3)

print(y**x)

x,*y,z = numbers
print(y)