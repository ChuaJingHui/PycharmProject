#defining variable
name = "Chua Jing Hui"
age = 16
height = 1.6
is_student = True

print(name)
print(age)
print(height)
print(is_student)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


#Activity 1
score=10
print(score)
score=score+15
print(score)
print("\n")

#Activity 2
state="Penang"
country="Malaysia"
place_of_birth=print(state,country)

combining_variable=str(score)+" "+state
print(combining_variable)

nom1="25"
nom1=int(nom1)
print(nom1 , type(nom1))

nom2=18
nom2=str(nom2)
print(nom2 , type(nom2))

nom3=3.8
nom3=int(nom3)
print(nom3 , type(nom3))

nom4=1
nom4=bool(nom4)
print(nom4 , type(nom4))

#Activity 3
x="3"
y=3

sum_float=float(x)+float(y)
sum_int=int(x)+y

print("\n")
print(sum_float,type(sum_float))
print(sum_int,type(sum_int))
print("\n")

#Creating List
my_list=[10,7.0,"Thong Thong"]
print(my_list[0])
print(my_list[1])
print(my_list[2])

print("\n")

#Adding item to list by changing the item
my_list_2=["apples","oranges","watermelon"]
my_list_2[1]="chocolate"
print(my_list_2)

print("\n")

#Adding item into list
my_list_3=["apples","oranges","watermelon"]
my_list_3.append("kiwi")
print(my_list_3)

print("\n")

#Removing item directly
my_list_3.remove("apples")
print(my_list_3)

print("\n")

#Removing item using index of item
my_list_3.pop(my_list_3.index("kiwi"))
print(my_list_3)

print("\n")

#Show the number of elements in the list
fruit=["apple","banana","orange","grape"]
print(len(fruit))

print("\n")

#Practice 1
numbers=[3,6,9,12,15]
numbers[3]=11
numbers.insert(1,7)
print(numbers)

print("\n")

#Practice 2
values=[2,5,8,3,9,1]
doubled_values = []
for value in values:
    doubled_values.append(value*2)
    value+=1

print(values)
print(doubled_values)