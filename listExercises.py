# You can use split and have characters by lists
message = ("Hi my name is Eren").split()

print(message[4])

# Sum of lists
list1 = ['one','two','three']
list2 = ['four','five','six']

sum_of_lists = list1 + list2
print(sum_of_lists)

#You can print the length
print(len(sum_of_lists))

#Create list of car brands: "Bmw, Mercedes, Opel, Mazda"
cars = ['Bmw','Mercedes','Opel', 'Mazda']
#How many elements this list has ?
print(len(cars))
#What are the first element and last element of this List?
print(cars[0])
print(cars[3])
#Change Mazda with Toyota (-1 also the last element)
cars[-1] = 'Toyota'
#Check if Mercedes is cars element
result = cars
result = 'Mercedes' in cars
print(result)
#What is the -2. index of the List
result = cars[-2]
print(result)


#Take the first 3 elements of the List
print(cars[:3])
#Add Totoya and Renault for last 2
cars[-2:] = ['Toyota','Renault']
print(cars)
#Add more car brands like : Audi and Nissan
cars+=['Audi','Nissan']
print(cars)
#Remove last element of the List
cars.pop()
print(cars)
#Print elements from end to the beginning
result = cars[::-1]
print(result)


studentA = ['Yigit','Bilgi',2010, [70,60,70]]
studentB = ['Sena Turan', 1999, [80,80,70]]
studentC = ['Ahmet Turan', 1998 ,[80,70,90]]

result1 = f" {studentA[0]} {studentA[1]} is {2026-studentA[2]} years old and GPA is {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3} "
print(result1)