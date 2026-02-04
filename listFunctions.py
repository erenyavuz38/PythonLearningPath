names = ['Ali', 'Yagmur', 'Hakan','Deniz']
years = [1998, 2000, 1998, 1987]
#Add name of "Cenk" at the end of the list of names

names.append('Cenk')

#Add name of "Sena" beginning of the list of names
names.insert(0, 'Sena')
#Find index number of 'Deniz'
index = names.index('Deniz')
print(index)
#Delete name of 'Deniz'from the list
names.remove('Deniz') #or pop(4)

#is 'Ali' one of the part of list?
result = 'Ali' in names
print(result)

#reverse List
names.reverse()
print(names)
#Sort elements of List alphabetically
names.sort()

#sort list of years
#str = "Chevrolet,Dacia" make this str List
str = "Chevrolet,Dacia"
result = str.split(',')
#Find min and max values of years

min_value = min(years)
max_value = max(years)
print(min_value,max_value)
#How many result of 1998 in years?
resultun = years.count(1998)
print(resultun)
print(result)
years.sort()
print(names)
print(years)

#delete all of em in years
years.clear()
print(years)

# get 3 values from user and keep in in brands
brands = []
brand = input("Brand: ")
brands.append(brand)

brand = input("Brand: ")
brands.append(brand)
brand = input("Brand: ")
brands.append(brand)

print(brands)